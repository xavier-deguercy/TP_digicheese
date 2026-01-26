(function(){
  const cfg = window.DC_CONFIG;
  const EP = cfg.ENDPOINTS.conditionnements;
  const F = cfg.FIELDS.conditionnement;

  const { apiFetch, clearStoredAuthValue } = window.DC_API;
  const { setFlash, clearFlash, pick, normalizeList } = window.DC_UI;

  const tbody = document.getElementById("tbody");
  const q = document.getElementById("q");

  const modal = document.getElementById("modal");
  const form = document.getElementById("formCondit");

  const idEl = document.getElementById("id");
  const libEl = document.getElementById("lib");
  const poidsEl = document.getElementById("poids");
  const prixEl = document.getElementById("prix");
  const ordreEl = document.getElementById("ordre");
  const btnDelete = document.getElementById("btnDelete");

  let cache = [];

  function showModal(isOpen){ modal.classList.toggle("hidden", !isOpen); }
  function resetForm(){
    idEl.value = "";
    libEl.value = "";
    poidsEl.value = "";
    prixEl.value = "";
    ordreEl.value = "";
    btnDelete.style.display = "none";
  }

  function render(list){
    const query = (q.value || "").toLowerCase();
    const filtered = list.filter(o => {
      const lib = String(pick(o, [F.lib, "lib_condit", "libelle", "name", "lib"], "")).toLowerCase();
      return !query || lib.includes(query);
    });

    if (!filtered.length) {
      tbody.innerHTML = '<tr><td colspan="6" class="muted">Aucun conditionnement.</td></tr>';
      return;
    }

    tbody.innerHTML = filtered.map(o => {
      const id = pick(o, [F.id, "id_condit", "id"], "");
      const lib = pick(o, [F.lib, "lib_condit", "libelle", "name", "lib"], "");
      const poids = pick(o, [F.poids, "poids_condit", "poids"], "");
      const prix = pick(o, [F.prix, "prix_condit", "prix"], "");
      const ordre = pick(o, [F.ordre, "ordre_imp", "ordre"], "");

      return `
        <tr>
          <td>${id}</td>
          <td>${escapeHtml(lib)}</td>
          <td>${poids}</td>
          <td>${prix}</td>
          <td>${ordre}</td>
          <td>
            <div class="table-actions">
              <button class="btn sm ghost" data-action="edit" data-id="${id}">Éditer</button>
              <button class="btn sm" data-action="delete" data-id="${id}">Supprimer</button>
            </div>
          </td>
        </tr>
      `;
    }).join("");
  }

  function escapeHtml(str){
    return String(str)
      .replaceAll("&","&amp;")
      .replaceAll("<","&lt;")
      .replaceAll(">","&gt;")
      .replaceAll('"',"&quot;")
      .replaceAll("'","&#039;");
  }

  async function load(){
    clearFlash();
    tbody.innerHTML = '<tr><td colspan="6" class="muted">Chargement…</td></tr>';
    try {
      const data = await apiFetch(`${EP}`, { method: "GET" });
      cache = normalizeList(data);
      render(cache);
      setFlash("ok", "Liste chargée", `${cache.length} conditionnement(s) récupéré(s).`);
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err && err.message) ? err.message : String(err);
      setFlash("bad", "Erreur API (GET)", detail);
      tbody.innerHTML = '<tr><td colspan="6" class="muted">Erreur de chargement.</td></tr>';
    }
  }

  function openCreate(){
    resetForm();
    document.getElementById("modalTitle").textContent = "Créer un conditionnement";
    showModal(true);
  }

  function openEdit(obj){
    resetForm();
    document.getElementById("modalTitle").textContent = "Éditer un conditionnement";

    const id = pick(obj, [F.id, "id_condit", "id"], "");
    idEl.value = id;

    libEl.value = pick(obj, [F.lib, "lib_condit"], "");
    poidsEl.value = pick(obj, [F.poids, "poids_condit"], "");
    prixEl.value = pick(obj, [F.prix, "prix_condit"], "");
    ordreEl.value = pick(obj, [F.ordre, "ordre_imp"], "");

    btnDelete.style.display = "inline-flex";
    showModal(true);
  }

  async function save(e){
    e.preventDefault();
    clearFlash();

    const isEdit = Boolean(idEl.value);
    const id = idEl.value;

    const body = {};
    body[F.lib] = libEl.value.trim();
    if (poidsEl.value !== "") body[F.poids] = parseInt(poidsEl.value, 10);
    if (prixEl.value !== "") body[F.prix] = String(prixEl.value); // souvent côté API c'est un Decimal sérialisé en string
    if (ordreEl.value !== "") body[F.ordre] = parseInt(ordreEl.value, 10);

    try {
      if (!body[F.lib]) {
        setFlash("warn", "Validation", "Le libellé est obligatoire.");
        return;
      }

      if (!isEdit) {
        await apiFetch(`${EP}`, { method: "POST", body });
        setFlash("ok", "Créé", "Conditionnement créé en base.");
      } else {
        await apiFetch(`${EP}/${encodeURIComponent(id)}`, { method: "PATCH", body });
        setFlash("ok", "Mis à jour", "Conditionnement modifié en base.");
      }

      showModal(false);
      await load();
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err && err.message) ? err.message : String(err);
      setFlash("bad", isEdit ? "Erreur API (PATCH)" : "Erreur API (POST)", detail);
    }
  }

  async function delById(id){
    clearFlash();
    try {
      await apiFetch(`${EP}/${encodeURIComponent(id)}`, { method: "DELETE" });
      setFlash("ok", "Supprimé", "Conditionnement supprimé.");
      showModal(false);
      await load();
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err && err.message) ? err.message : String(err);
      setFlash("bad", "Erreur API (DELETE)", detail);
    }
  }

  // Events
  document.getElementById("btnRefresh").addEventListener("click", load);
  document.getElementById("btnCreate").addEventListener("click", openCreate);
  document.getElementById("btnClose").addEventListener("click", () => showModal(false));
  q.addEventListener("input", () => render(cache));
  form.addEventListener("submit", save);

  btnDelete.addEventListener("click", () => {
    const id = idEl.value;
    if (!id) return;
    if (confirm("Confirmer la suppression du conditionnement #" + id + " ?")) delById(id);
  });

  tbody.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    const action = btn.getAttribute("data-action");
    const id = btn.getAttribute("data-id");
    const obj = cache.find(o => String(pick(o, [F.id, "id_condit", "id"], "")) === String(id));

    if (action === "edit" && obj) openEdit(obj);
    if (action === "delete" && id) {
      if (confirm("Confirmer la suppression du conditionnement #" + id + " ?")) delById(id);
    }
  });

  document.getElementById("logoutLink").addEventListener("click", () => clearStoredAuthValue());

  // Init
  load();
})();
