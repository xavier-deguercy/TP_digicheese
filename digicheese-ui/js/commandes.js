(function(){
  const cfg = window.DC_CONFIG;
  const EP = cfg.ENDPOINTS.commandes;
  const F = cfg.FIELDS.commande;
  const { apiFetch } = window.DC_API;
  const { setFlash, clearFlash, normalizeList } = window.DC_UI;

  const tbody = document.getElementById("tbody");
  const q = document.getElementById("q");
  const statusFilter = document.getElementById("statusFilter");
  const modal = document.getElementById("modal");
  const form = document.getElementById("formCommande");
  const idEl = document.getElementById("id");
  const dateEl = document.getElementById("dateCommande");
  const clientEl = document.getElementById("clientCommande");
  const conditionnementEl = document.getElementById("conditionnementCommande");
  const nbColisEl = document.getElementById("nbColis");
  const timbreClientEl = document.getElementById("timbreClient");
  const timbreCodeEl = document.getElementById("timbreCode");
  const btnDelete = document.getElementById("btnDelete");

  let commandes = [];
  let clients = [];
  let conditionnements = [];
  let originalConditionnement = "";

  function escapeHtml(value){
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function clientLabel(id){
    const item = clients.find(c => String(c.id_client) === String(id));
    if (!item) return `Client #${id}`;
    const fullName = [item.prenom_client, item.nom_client].filter(Boolean).join(" ");
    return fullName || item.email_client || `Client #${id}`;
  }

  function conditionnementLabel(id){
    if (id === null || id === undefined || id === "") return "À définir";
    const item = conditionnements.find(c => String(c.id_condit) === String(id));
    return item ? (item.lib_condit || `Conditionnement #${id}`) : `Conditionnement #${id}`;
  }

  function fillSelects(){
    clientEl.innerHTML = '<option value="">Sélectionner un client</option>' + clients.map(c =>
      `<option value="${c.id_client}">${escapeHtml(clientLabel(c.id_client))}</option>`
    ).join("");
    conditionnementEl.innerHTML = '<option value="">À définir plus tard</option>' + conditionnements.map(c =>
      `<option value="${c.id_condit}">${escapeHtml(conditionnementLabel(c.id_condit))}</option>`
    ).join("");
  }

  function render(){
    const query = q.value.trim().toLowerCase();
    const state = statusFilter.value;
    const filtered = commandes.filter(item => {
      const archived = Boolean(item[F.archivee]);
      if (state === "active" && archived) return false;
      if (state === "archived" && !archived) return false;
      const haystack = [item[F.id], item[F.date], clientLabel(item[F.client])].join(" ").toLowerCase();
      return !query || haystack.includes(query);
    });

    if (!filtered.length) {
      tbody.innerHTML = '<tr><td colspan="7" class="muted">Aucune commande.</td></tr>';
      return;
    }

    tbody.innerHTML = filtered.map(item => {
      const id = item[F.id];
      const archived = Boolean(item[F.archivee]);
      return `<tr>
        <td>${id}</td>
        <td>${escapeHtml(item[F.date])}</td>
        <td>${escapeHtml(clientLabel(item[F.client]))}</td>
        <td>${escapeHtml(conditionnementLabel(item[F.conditionnement]))}</td>
        <td>${item[F.nbColis] ?? "À vérifier"}</td>
        <td><span class="pill ${archived ? "warn" : "ok"}">${archived ? "Archivée" : "Active"}</span></td>
        <td><div class="table-actions">
          <a class="btn sm ghost" href="commande-details.html?commande_id=${id}">Détails</a>
          ${archived ? "" : `<button class="btn sm ghost" data-action="edit" data-id="${id}">Éditer</button>`}
          <button class="btn sm ghost" data-action="archive" data-id="${id}">${archived ? "Désarchiver" : "Archiver"}</button>
          ${archived ? "" : `<button class="btn sm" data-action="delete" data-id="${id}">Supprimer</button>`}
        </div></td>
      </tr>`;
    }).join("");
  }

  function showModal(open){ modal.classList.toggle("hidden", !open); }

  function resetForm(){
    idEl.value = "";
    dateEl.value = new Date().toISOString().slice(0, 10);
    clientEl.value = "";
    conditionnementEl.value = "";
    nbColisEl.value = "";
    timbreClientEl.value = "";
    timbreCodeEl.value = "";
    originalConditionnement = "";
    btnDelete.style.display = "none";
  }

  function openCreate(){
    resetForm();
    document.getElementById("modalTitle").textContent = "Créer une commande";
    showModal(true);
  }

  function openEdit(item){
    resetForm();
    document.getElementById("modalTitle").textContent = `Modifier la commande #${item[F.id]}`;
    idEl.value = item[F.id];
    dateEl.value = item[F.date];
    clientEl.value = item[F.client];
    conditionnementEl.value = item[F.conditionnement] ?? "";
    originalConditionnement = conditionnementEl.value;
    nbColisEl.value = item[F.nbColis] ?? "";
    timbreClientEl.value = item[F.timbreClient] ?? "";
    timbreCodeEl.value = item[F.timbreCode] ?? "";
    btnDelete.style.display = "inline-flex";
    showModal(true);
  }

  async function load(){
    clearFlash();
    tbody.innerHTML = '<tr><td colspan="7" class="muted">Chargement…</td></tr>';
    try {
      const [commandesData, clientsData, conditionnementsData] = await Promise.all([
        apiFetch(EP),
        apiFetch(cfg.ENDPOINTS.clients),
        apiFetch(cfg.ENDPOINTS.conditionnements)
      ]);
      commandes = normalizeList(commandesData);
      clients = normalizeList(clientsData);
      conditionnements = normalizeList(conditionnementsData);
      fillSelects();
      render();
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err.message || String(err));
      setFlash("bad", "Erreur de chargement", detail);
      tbody.innerHTML = '<tr><td colspan="7" class="muted">Erreur de chargement.</td></tr>';
    }
  }

  async function save(event){
    event.preventDefault();
    clearFlash();
    const editing = Boolean(idEl.value);
    const selectedConditionnement = conditionnementEl.value;
    const body = {
      [F.date]: dateEl.value,
      [F.client]: Number(clientEl.value),
      [F.conditionnement]: selectedConditionnement ? Number(selectedConditionnement) : null,
      [F.nbColis]: nbColisEl.value ? Number(nbColisEl.value) : null,
      [F.timbreClient]: timbreClientEl.value.trim() || null,
      [F.timbreCode]: timbreCodeEl.value.trim() || null
    };
    if (!editing) body[F.archivee] = false;
    if (editing && selectedConditionnement !== originalConditionnement) body[F.nbColis] = null;

    try {
      await apiFetch(editing ? `${EP}/${encodeURIComponent(idEl.value)}` : EP, {
        method: editing ? "PATCH" : "POST",
        body
      });
      showModal(false);
      await load();
      setFlash("ok", editing ? "Commande mise à jour" : "Commande créée", "Les données ont été enregistrées.");
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err.message || String(err));
      setFlash("bad", "Enregistrement impossible", detail);
    }
  }

  async function setArchived(id, archived){
    try {
      await apiFetch(`${EP}/${encodeURIComponent(id)}`, {method: "PATCH", body: {[F.archivee]: archived}});
      await load();
      setFlash("ok", archived ? "Commande archivée" : "Commande désarchivée", `Commande #${id}`);
    } catch (err) {
      setFlash("bad", "Action impossible", err && err.data ? JSON.stringify(err.data) : err.message);
    }
  }

  async function deleteById(id){
    try {
      await apiFetch(`${EP}/${encodeURIComponent(id)}`, {method: "DELETE"});
      showModal(false);
      await load();
      setFlash("ok", "Commande supprimée", `Commande #${id}`);
    } catch (err) {
      setFlash("bad", "Suppression impossible", err && err.data ? JSON.stringify(err.data) : err.message);
    }
  }

  conditionnementEl.addEventListener("change", () => { nbColisEl.value = ""; });
  q.addEventListener("input", render);
  statusFilter.addEventListener("change", render);
  document.getElementById("btnRefresh").addEventListener("click", load);
  document.getElementById("btnCreate").addEventListener("click", openCreate);
  document.getElementById("btnClose").addEventListener("click", () => showModal(false));
  form.addEventListener("submit", save);
  btnDelete.addEventListener("click", () => {
    if (idEl.value && confirm(`Supprimer définitivement la commande #${idEl.value} ?`)) deleteById(idEl.value);
  });
  tbody.addEventListener("click", event => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;
    const id = button.dataset.id;
    const item = commandes.find(value => String(value[F.id]) === String(id));
    if (!item) return;
    if (button.dataset.action === "edit") openEdit(item);
    if (button.dataset.action === "archive") setArchived(id, !item[F.archivee]);
    if (button.dataset.action === "delete" && confirm(`Supprimer définitivement la commande #${id} ?`)) deleteById(id);
  });

  load();
})();
