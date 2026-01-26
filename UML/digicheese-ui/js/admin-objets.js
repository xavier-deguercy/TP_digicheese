(function(){
  const cfg = window.DC_CONFIG;
  const EP = cfg.ENDPOINTS.objets; // "/objets"
  const F = cfg.FIELDS.objet;      // {id, lib, taille, prix}

  const { apiFetch, clearStoredAuthValue } = window.DC_API;
  const { setFlash, clearFlash, pick, normalizeList } = window.DC_UI;

  const tbody = document.getElementById("tbody");
  const q = document.getElementById("q");

  const modal = document.getElementById("modal");
  const form = document.getElementById("formObjet");

  const idEl = document.getElementById("id");
  const nomEl = document.getElementById("nom");
  const tailleEl = document.getElementById("taille");
  const prixEl = document.getElementById("prix");

  const btnDelete = document.getElementById("btnDelete");

  let cache = [];

  function showModal(isOpen){ modal.classList.toggle("hidden", !isOpen); }
  function resetForm(){
    idEl.value = "";
    nomEl.value = "";
    tailleEl.value = "";
    prixEl.value = "";
    btnDelete.style.display = "none";
  }

  function escapeHtml(str){
    return String(str)
      .replaceAll("&","&amp;")
      .replaceAll("<","&lt;")
      .replaceAll(">","&gt;")
      .replaceAll('"',"&quot;")
      .replaceAll("'","&#039;");
  }

  function render(list){
    const query = (q.value || "").toLowerCase();
    const filtered = list.filter(o => {
      const nom = String(pick(o, [F.lib, "nom_obj", "nom"], "")).toLowerCase();
      return !query || nom.includes(query);
    });

    if (!filtered.length) {
      tbody.innerHTML = '<tr><td colspan="6" class="muted">Aucun objet.</td></tr>';
      return;
    }

    tbody.innerHTML = filtered.map(o => {
      const id = pick(o, [F.id, "id_objet", "id"], "");
      const nom = pick(o, [F.lib, "nom_obj", "nom"], "");
      const taille = pick(o, [F.taille, "taille_obj", "taille"], "—");
      const prix = pick(o, [F.prix, "prix_obj", "prix"], "0.0000");

      return `
        <tr>
          <td>${id}</td>
          <td>${escapeHtml(nom)}</td>
          <td>${escapeHtml(taille ?? "—")}</td>
          <td>${prix ?? ""}</td>
          <td class="muted">—</td>
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

  async function load(){
    clearFlash();
    tbody.innerHTML = '<tr><td colspan="6" class="muted">Chargement…</td></tr>';
    try {
      const data = await apiFetch(`${EP}`, { method: "GET" });
      cache = normalizeList(data);
      render(cache);
      setFlash("ok", "Liste chargée", `${cache.length} objet(s) récupéré(s).`);
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err && err.message) ? err.message : String(err);
      setFlash("bad", "Erreur API (GET)", detail);
      tbody.innerHTML = '<tr><td colspan="6" class="muted">Erreur de chargement.</td></tr>';
    }
  }

  function openCreate(){
    resetForm();
    document.getElementById("modalTitle").textContent = "Créer un objet";
    showModal(true);
  }

  function openEdit(obj){
    resetForm();
    document.getElementById("modalTitle").textContent = "Éditer un objet";

    const id = pick(obj, [F.id, "id_objet", "id"], "");
    idEl.value = id;

    nomEl.value = pick(obj, [F.lib, "nom_obj", "nom"], "");
    tailleEl.value = pick(obj, [F.taille, "taille_obj", "taille"], "");
    prixEl.value = pick(obj, [F.prix, "prix_obj", "prix"], "");

    btnDelete.style.display = "inline-flex";
    showModal(true);
  }

  async function save(e){
    e.preventDefault();
    clearFlash();

    const isEdit = Boolean(idEl.value);
    const id = idEl.value;

    const body = {};
    body[F.lib] = nomEl.value.trim();
    if (tailleEl.value.trim() !== "") body[F.taille] = tailleEl.value.trim();
    if (prixEl.value !== "") body[F.prix] = String(prixEl.value);

    try {
      if (!body[F.lib]) {
        setFlash("warn", "Validation", "Le nom (nom_obj) est obligatoire.");
        return;
      }

      if (!isEdit) {
        await apiFetch(`${EP}`, { method: "POST", body });
        setFlash("ok", "Créé", "Objet créé en base.");
      } else {
        await apiFetch(`${EP}/${encodeURIComponent(id)}`, { method: "PATCH", body });
        setFlash("ok", "Mis à jour", "Objet modifié en base.");
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
      setFlash("ok", "Supprimé", "Objet supprimé.");
      showModal(false);
      await load();
    } catch (err) {
      const detail = err && err.data ? JSON.stringify(err.data) : (err && err.message) ? err.message : String(err);
      setFlash("bad", "Erreur API (DELETE)", detail);
    }
  }

  document.getElementById("btnRefresh").addEventListener("click", load);
  document.getElementById("btnCreate").addEventListener("click", openCreate);
  document.getElementById("btnClose").addEventListener("click", () => showModal(false));
  q.addEventListener("input", () => render(cache));
  form.addEventListener("submit", save);

  btnDelete.addEventListener("click", () => {
    const id = idEl.value;
    if (!id) return;
    if (confirm("Confirmer la suppression de l'objet #" + id + " ?")) delById(id);
  });

  tbody.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (!btn) return;
    const action = btn.getAttribute("data-action");
    const id = btn.getAttribute("data-id");
    const obj = cache.find(o => String(pick(o, [F.id, "id_objet", "id"], "")) === String(id));

    if (action === "edit" && obj) openEdit(obj);
    if (action === "delete" && id) {
      if (confirm("Confirmer la suppression de l'objet #" + id + " ?")) delById(id);
    }
  });

  document.getElementById("logoutLink").addEventListener("click", () => clearStoredAuthValue());
  load();
})();
