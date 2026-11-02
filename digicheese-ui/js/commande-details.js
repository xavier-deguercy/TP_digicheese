(function(){
  const cfg = window.DC_CONFIG;
  const { apiFetch } = window.DC_API;
  const { setFlash, clearFlash, normalizeList } = window.DC_UI;
  const commandeId = Number(new URLSearchParams(window.location.search).get("commande_id"));

  const tbody = document.getElementById("tbody");
  const modal = document.getElementById("modal");
  const form = document.getElementById("formDetail");
  const idEl = document.getElementById("idDetail");
  const objetEl = document.getElementById("objetDetail");
  const quantiteEl = document.getElementById("quantiteDetail");
  const commentaireEl = document.getElementById("commentaireDetail");
  const btnCreate = document.getElementById("btnCreate");
  const btnDelete = document.getElementById("btnDelete");

  let commande = null;
  let details = [];
  let objets = [];
  let clients = [];

  function escapeHtml(value){
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function objetById(id){
    return objets.find(item => String(item.id_objet) === String(id));
  }

  function objetLabel(id){
    const objet = objetById(id);
    if (!objet) return `Objet #${id}`;
    return `${objet.nom_obj || `Objet #${id}`}${objet.indisp_obj ? " — indisponible" : ""}`;
  }

  function clientLabel(id){
    const client = clients.find(item => String(item.id_client) === String(id));
    if (!client) return `Client #${id}`;
    return [client.prenom_client, client.nom_client].filter(Boolean).join(" ") || client.email_client || `Client #${id}`;
  }

  function showModal(open){ modal.classList.toggle("hidden", !open); }

  function fillObjectSelect(selectedId = ""){
    const usedIds = new Set(details.map(item => String(item.id_objet)));
    const available = objets.filter(item => {
      const selected = String(item.id_objet) === String(selectedId);
      return (!item.indisp_obj || selected) && (selected || !usedIds.has(String(item.id_objet)));
    });
    objetEl.innerHTML = '<option value="">Sélectionner un objet</option>' + available.map(item =>
      `<option value="${item.id_objet}">${escapeHtml(objetLabel(item.id_objet))}</option>`
    ).join("");
    objetEl.value = selectedId ? String(selectedId) : "";
  }

  function renderHeader(){
    const archived = Boolean(commande.b_archive);
    document.getElementById("pageTitle").textContent = `Commande #${commande.id_commande}`;
    document.getElementById("commandeSummary").textContent = `${commande.date_commande} — ${clientLabel(commande.id_client)}`;
    const state = document.getElementById("commandeState");
    state.textContent = archived ? "Archivée — lecture seule" : "Active";
    state.className = `pill ${archived ? "warn" : "ok"}`;
    document.getElementById("nbColisState").textContent = `Nombre de colis : ${commande.nb_colis ?? "à vérifier"}`;
    btnCreate.style.display = archived ? "none" : "inline-flex";
  }

  function render(){
    if (!details.length) {
      tbody.innerHTML = '<tr><td colspan="5" class="muted">Aucune ligne dans cette commande.</td></tr>';
      return;
    }
    const archived = Boolean(commande.b_archive);
    tbody.innerHTML = details.map(item => `<tr>
      <td>${item.id_detail_commande}</td>
      <td>${escapeHtml(objetLabel(item.id_objet))}</td>
      <td>${item.quantite}</td>
      <td>${escapeHtml(item.commentaire || "—")}</td>
      <td><div class="table-actions">
        ${archived ? '<span class="muted">Lecture seule</span>' : `<button class="btn sm ghost" data-action="edit" data-id="${item.id_detail_commande}">Éditer</button><button class="btn sm" data-action="delete" data-id="${item.id_detail_commande}">Supprimer</button>`}
      </div></td>
    </tr>`).join("");
  }

  function resetForm(){
    idEl.value = "";
    fillObjectSelect();
    quantiteEl.value = "1";
    commentaireEl.value = "";
    btnDelete.style.display = "none";
  }

  function openCreate(){
    resetForm();
    document.getElementById("modalTitle").textContent = "Ajouter un objet";
    showModal(true);
  }

  function openEdit(detail){
    idEl.value = detail.id_detail_commande;
    fillObjectSelect(detail.id_objet);
    quantiteEl.value = detail.quantite;
    commentaireEl.value = detail.commentaire || "";
    btnDelete.style.display = "inline-flex";
    document.getElementById("modalTitle").textContent = `Modifier la ligne #${detail.id_detail_commande}`;
    showModal(true);
  }

  async function load(){
    clearFlash();
    if (!Number.isInteger(commandeId) || commandeId < 1) {
      setFlash("bad", "Commande invalide", "L'identifiant de commande manque dans l'URL.");
      btnCreate.style.display = "none";
      tbody.innerHTML = '<tr><td colspan="5" class="muted">Commande invalide.</td></tr>';
      return;
    }
    tbody.innerHTML = '<tr><td colspan="5" class="muted">Chargement…</td></tr>';
    try {
      const [commandeData, detailsData, objetsData, clientsData] = await Promise.all([
        apiFetch(`${cfg.ENDPOINTS.commandes}/${commandeId}`),
        apiFetch(`${cfg.ENDPOINTS.detailsCommandes}?commande_id=${commandeId}`),
        apiFetch(cfg.ENDPOINTS.objets),
        apiFetch(cfg.ENDPOINTS.clients)
      ]);
      commande = commandeData;
      details = normalizeList(detailsData);
      objets = normalizeList(objetsData);
      clients = normalizeList(clientsData);
      renderHeader();
      render();
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err.message || String(err));
      setFlash("bad", "Chargement impossible", detail);
      btnCreate.style.display = "none";
      tbody.innerHTML = '<tr><td colspan="5" class="muted">Erreur de chargement.</td></tr>';
    }
  }

  async function save(event){
    event.preventDefault();
    clearFlash();
    const editing = Boolean(idEl.value);
    const body = {
      id_objet: Number(objetEl.value),
      quantite: Number(quantiteEl.value),
      commentaire: commentaireEl.value.trim() || null
    };
    if (!editing) body.id_commande = commandeId;
    try {
      await apiFetch(
        editing ? `${cfg.ENDPOINTS.detailsCommandes}/${encodeURIComponent(idEl.value)}` : cfg.ENDPOINTS.detailsCommandes,
        {method: editing ? "PATCH" : "POST", body}
      );
      showModal(false);
      await load();
      setFlash("ok", editing ? "Ligne mise à jour" : "Ligne ajoutée", "Le nombre de colis est maintenant à vérifier.");
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err.message || String(err));
      setFlash("bad", "Enregistrement impossible", detail);
    }
  }

  async function deleteById(id){
    try {
      await apiFetch(`${cfg.ENDPOINTS.detailsCommandes}/${encodeURIComponent(id)}`, {method: "DELETE"});
      showModal(false);
      await load();
      setFlash("ok", "Ligne supprimée", "Le nombre de colis est maintenant à vérifier.");
    } catch (err) {
      setFlash("bad", "Suppression impossible", err && err.data ? JSON.stringify(err.data) : err.message);
    }
  }

  document.getElementById("btnRefresh").addEventListener("click", load);
  btnCreate.addEventListener("click", openCreate);
  document.getElementById("btnClose").addEventListener("click", () => showModal(false));
  form.addEventListener("submit", save);
  btnDelete.addEventListener("click", () => {
    if (idEl.value && confirm(`Supprimer la ligne #${idEl.value} ?`)) deleteById(idEl.value);
  });
  tbody.addEventListener("click", event => {
    const button = event.target.closest("button[data-action]");
    if (!button) return;
    const detail = details.find(item => String(item.id_detail_commande) === String(button.dataset.id));
    if (!detail) return;
    if (button.dataset.action === "edit") openEdit(detail);
    if (button.dataset.action === "delete" && confirm(`Supprimer la ligne #${detail.id_detail_commande} ?`)) deleteById(detail.id_detail_commande);
  });

  load();
})();
