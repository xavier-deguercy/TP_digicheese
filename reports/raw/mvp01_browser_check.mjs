import fs from "node:fs";

const API = "http://127.0.0.1:8000";
const UI = "http://127.0.0.1:5502/commandes.html";

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
const commune = await api("/commune", {method: "POST", body: {dep: "34", cp: "34000", ville: `UI MVP01 ${stamp}`}});
const adresse = await api("/adresse", {method: "POST", body: {rue: "1 rue UI", compAdresse: "", id_commune: commune.id_commune}});
const client = await api("/clients", {method: "POST", body: {email_client: `ui-${stamp}@example.com`, nom_client: "Navigateur", prenom_client: "Test", adresse1_client: adresse.id_adresse}});
const cond1 = await api("/conditionnements", {method: "POST", body: {lib_condit: `Boite UI A ${stamp}`, poids_condit: 250, prix_condit: 1}});
const cond2 = await api("/conditionnements", {method: "POST", body: {lib_condit: `Boite UI B ${stamp}`, poids_condit: 500, prix_condit: 2}});

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
await command("Page.navigate", {url: UI});
await waitFor("document.readyState === 'complete'");
await waitFor("document.querySelector('#clientCommande')?.options.length > 1 && document.querySelector('#conditionnementCommande')?.options.length > 2");

const initial = await evaluate(`({title: document.title, heading: document.querySelector('h1')?.textContent, headerLink: Boolean([...document.querySelectorAll('a')].find(a => a.textContent.trim() === 'Commandes'))})`);

await evaluate(`document.querySelector('#btnCreate').click()`);
await waitFor("!document.querySelector('#modal').classList.contains('hidden')");
await evaluate(`(() => {
  document.querySelector('#dateCommande').value = '2026-09-07';
  document.querySelector('#clientCommande').value = '${client.id_client}';
  document.querySelector('#conditionnementCommande').value = '${cond1.id_condit}';
  document.querySelector('#nbColis').value = '2';
  document.querySelector('#timbreClient').value = 'UI-E2E';
  document.querySelector('#formCommande').requestSubmit();
})()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('Commande cr') && document.querySelector('#tbody tr td')?.textContent !== 'Aucune commande.'");

const createdId = await evaluate(`Number(document.querySelector('#tbody tr td').textContent.trim())`);
await evaluate(`document.querySelector('button[data-action="edit"][data-id="${createdId}"]').click()`);
await waitFor("!document.querySelector('#modal').classList.contains('hidden')");
const beforeReset = await evaluate(`document.querySelector('#nbColis').value`);
await evaluate(`(() => {
  const select = document.querySelector('#conditionnementCommande');
  select.value = '${cond2.id_condit}';
  select.dispatchEvent(new Event('change', {bubbles: true}));
})()`);
const afterReset = await evaluate(`document.querySelector('#nbColis').value`);
await evaluate(`document.querySelector('#formCommande').requestSubmit()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('mise')");
const afterConditionnementChange = await api(`/commandes/${createdId}`);

await evaluate(`document.querySelector('button[data-action="archive"][data-id="${createdId}"]').click()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('archiv')");
await evaluate(`(() => { const select = document.querySelector('#statusFilter'); select.value = 'archived'; select.dispatchEvent(new Event('change', {bubbles: true})); })()`);
await waitFor(`Boolean(document.querySelector('button[data-action="archive"][data-id="${createdId}"]'))`);
const archivedControls = await evaluate(`({edit: Boolean(document.querySelector('button[data-action="edit"][data-id="${createdId}"]')), remove: Boolean(document.querySelector('button[data-action="delete"][data-id="${createdId}"]')), archiveLabel: document.querySelector('button[data-action="archive"][data-id="${createdId}"]').textContent.trim()})`);

await evaluate(`document.querySelector('button[data-action="archive"][data-id="${createdId}"]').click()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('sarchiv')");
await evaluate(`(() => { const select = document.querySelector('#statusFilter'); select.value = 'active'; select.dispatchEvent(new Event('change', {bubbles: true})); window.confirm = () => true; })()`);
await waitFor(`Boolean(document.querySelector('button[data-action="delete"][data-id="${createdId}"]'))`);
await evaluate(`document.querySelector('button[data-action="delete"][data-id="${createdId}"]').click()`);
await waitFor("document.querySelector('#flash')?.textContent.includes('supprim')");
const deletedStatus = await fetch(`${API}/commandes/${createdId}`).then(response => response.status);

const screenshot = await command("Page.captureScreenshot", {format: "png", captureBeyondViewport: true});
fs.writeFileSync("reports/raw/mvp01_commandes_browser.png", Buffer.from(screenshot.data, "base64"));

await api(`/conditionnements/${cond1.id_condit}`, {method: "DELETE"});
await api(`/conditionnements/${cond2.id_condit}`, {method: "DELETE"});
await api(`/clients/${client.id_client}`, {method: "DELETE"});
await api(`/adresse/${adresse.id_adresse}`, {method: "DELETE"});
await api(`/commune/${commune.id_commune}`, {method: "DELETE"});

ws.close();

const result = {
  initial,
  createdId,
  nbColisBeforeConditionnementChange: beforeReset,
  nbColisAfterUiReset: afterReset,
  persistedNbColisAfterChange: afterConditionnementChange.nb_colis,
  persistedConditionnement: afterConditionnementChange.id_conditionnement,
  archivedControls,
  deletedStatus,
  browserErrors,
  screenshot: "reports/raw/mvp01_commandes_browser.png",
};
console.log(JSON.stringify(result, null, 2));
