import fs from "node:fs";

const API = "http://127.0.0.1:8000";
const UI = "http://127.0.0.1:5502";

async function api(path, options = {}) {
  const response = await fetch(API + path, {
    ...options,
    headers: {"Content-Type": "application/json", ...(options.headers || {})},
    body: options.body && typeof options.body !== "string" ? JSON.stringify(options.body) : options.body,
  });
  const data = await response.json().catch(() => null);
  if (!response.ok) throw new Error(`${options.method || "GET"} ${path}: ${response.status} ${JSON.stringify(data)}`);
  return data;
}

const stamp = Date.now();
const commune = await api("/commune", {method: "POST", body: {dep: "34", cp: "34000", ville: `UI MVP02 ${stamp}`}});
const adresse = await api("/adresse", {method: "POST", body: {rue: "2 rue UI", compAdresse: "", id_commune: commune.id_commune}});
const client = await api("/clients", {method: "POST", body: {email_client: `ui-mvp02-${stamp}@example.com`, nom_client: "Navigateur", prenom_client: "MVP02", adresse1_client: adresse.id_adresse}});
const objet1 = await api("/objets", {method: "POST", body: {nom_obj: `Objet UI A ${stamp}`, prix_obj: 2, poids_obj: 100}});
const objet2 = await api("/objets", {method: "POST", body: {nom_obj: `Objet UI B ${stamp}`, prix_obj: 3, poids_obj: 120}});
const indisponible = await api("/objets", {method: "POST", body: {nom_obj: `Objet UI indisponible ${stamp}`, prix_obj: 4, poids_obj: 140, indisp_obj: true}});
const commande = await api("/commandes", {method: "POST", body: {date_commande: "2026-09-07", id_client: client.id_client, nb_colis: 2, b_archive: false}});

const pages = await fetch("http://127.0.0.1:9223/json/list").then(response => response.json());
const page = pages.find(item => item.type === "page");
if (!page) throw new Error("Aucune page Chrome disponible");
const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  ws.addEventListener("open", resolve, {once: true});
  ws.addEventListener("error", reject, {once: true});
});

let nextId = 0;
const pending = new Map();
const browserErrors = [];
ws.addEventListener("message", event => {
  const message = JSON.parse(event.data);
  if (message.id && pending.has(message.id)) {
    const {resolve, reject} = pending.get(message.id);
    pending.delete(message.id);
    if (message.error) reject(new Error(JSON.stringify(message.error)));
    else resolve(message.result);
  }
  if (message.method === "Runtime.exceptionThrown") browserErrors.push(message.params.exceptionDetails.text);
  if (message.method === "Log.entryAdded" && message.params.entry.level === "error") browserErrors.push(message.params.entry.text);
});

function command(method, params = {}) {
  const id = ++nextId;
  ws.send(JSON.stringify({id, method, params}));
  return new Promise((resolve, reject) => pending.set(id, {resolve, reject}));
}

async function evaluate(expression) {
  const result = await command("Runtime.evaluate", {expression, awaitPromise: true, returnByValue: true});
  if (result.exceptionDetails) throw new Error(result.exceptionDetails.text);
  return result.result.value;
}

async function waitFor(expression, timeoutMs = 6000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (await evaluate(expression)) return;
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  throw new Error(`Delai depasse: ${expression}`);
}

await command("Page.enable");
await command("Runtime.enable");
await command("Log.enable");
await command("Emulation.setDeviceMetricsOverride", {width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false});
await command("Page.navigate", {url: `${UI}/commandes.html`});
await waitFor(`Boolean(document.querySelector('a[href="commande-details.html?commande_id=${commande.id_commande}"]'))`);
const detailsLinkVisible = await evaluate(`document.querySelector('a[href="commande-details.html?commande_id=${commande.id_commande}"]').textContent.trim()`);
await evaluate(`document.querySelector('a[href="commande-details.html?commande_id=${commande.id_commande}"]').click()`);
await waitFor(`location.pathname.endsWith('/commande-details.html') && document.querySelector('#pageTitle')?.textContent === 'Commande #${commande.id_commande}'`);

await evaluate(`document.querySelector('#btnCreate').click()`);
await waitFor("!document.querySelector('#modal').classList.contains('hidden')");
const createOptions = await evaluate(`([...document.querySelector('#objetDetail').options].map(option => ({value: option.value, text: option.textContent})))`);
await evaluate(`(() => {
  document.querySelector('#objetDetail').value = '${objet1.id_objet}';
  document.querySelector('#quantiteDetail').value = '2';
  document.querySelector('#commentaireDetail').value = 'Parcours navigateur MVP-02';
  document.querySelector('#formDetail').requestSubmit();
})()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('Ligne ajout') && document.querySelector('#tbody tr td')?.textContent !== 'Aucune ligne dans cette commande.'");
const detailId = await evaluate(`Number(document.querySelector('#tbody tr td').textContent.trim())`);
const afterCreate = await api(`/commandes/${commande.id_commande}`);

await evaluate(`document.querySelector('#btnCreate').click()`);
await waitFor("!document.querySelector('#modal').classList.contains('hidden')");
const remainingOptions = await evaluate(`([...document.querySelector('#objetDetail').options].map(option => option.value).filter(Boolean))`);
await evaluate(`document.querySelector('#btnClose').click()`);

await evaluate(`document.querySelector('button[data-action="edit"]').click()`);
await waitFor("!document.querySelector('#modal').classList.contains('hidden')");
await evaluate(`(() => {
  document.querySelector('#quantiteDetail').value = '3';
  document.querySelector('#commentaireDetail').value = 'Commentaire modifie';
  document.querySelector('#formDetail').requestSubmit();
})()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('mise') && document.querySelector('#tbody').textContent.includes('Commentaire modifie')");

await api(`/commandes/${commande.id_commande}`, {method: "PATCH", body: {b_archive: true}});
await evaluate(`document.querySelector('#btnRefresh').click()`);
await waitFor("document.querySelector('#commandeState')?.textContent.includes('lecture seule')");
const archivedUi = await evaluate(`({createHidden: document.querySelector('#btnCreate').style.display === 'none', editButtons: document.querySelectorAll('button[data-action="edit"]').length, deleteButtons: document.querySelectorAll('button[data-action="delete"]').length, state: document.querySelector('#commandeState').textContent.trim()})`);

const screenshot = await command("Page.captureScreenshot", {format: "png", captureBeyondViewport: true});
fs.writeFileSync("reports/raw/mvp02_details_browser.png", Buffer.from(screenshot.data, "base64"));

await api(`/commandes/${commande.id_commande}`, {method: "PATCH", body: {b_archive: false}});
await evaluate(`document.querySelector('#btnRefresh').click()`);
await waitFor("document.querySelector('#commandeState')?.textContent === 'Active'");
await evaluate(`window.confirm = () => true; document.querySelector('button[data-action="delete"]').click()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('Ligne supprim') && document.querySelector('#tbody').textContent.includes('Aucune ligne')");
const deletedStatus = await fetch(`${API}/details-commandes/${detailId}`).then(response => response.status);

await api(`/commandes/${commande.id_commande}`, {method: "DELETE"});
await api(`/objets/${objet1.id_objet}`, {method: "DELETE"});
await api(`/objets/${objet2.id_objet}`, {method: "DELETE"});
await api(`/objets/${indisponible.id_objet}`, {method: "DELETE"});
await api(`/clients/${client.id_client}`, {method: "DELETE"});
await api(`/adresse/${adresse.id_adresse}`, {method: "DELETE"});
await api(`/commune/${commune.id_commune}`, {method: "DELETE"});
ws.close();

console.log(JSON.stringify({
  detailsLinkVisible,
  createOptionIds: createOptions.map(option => Number(option.value)).filter(Boolean),
  unavailableExcludedAtCreation: !createOptions.some(option => option.value === String(indisponible.id_objet)),
  usedObjectExcludedAfterCreation: !remainingOptions.includes(String(objet1.id_objet)),
  unusedObjectStillAvailable: remainingOptions.includes(String(objet2.id_objet)),
  nbColisAfterCreate: afterCreate.nb_colis,
  archivedUi,
  deletedStatus,
  browserErrors,
  screenshot: "reports/raw/mvp02_details_browser.png",
}, null, 2));
