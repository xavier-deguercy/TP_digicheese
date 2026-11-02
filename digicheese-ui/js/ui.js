/* Digicheese Admin UI — UI helpers */
(function () {
  function setFlash(type, title, detail) {
    const box = document.getElementById("flash");
    if (!box) return;

    const pill = box.querySelector("[data-flash-pill]");
    const h = box.querySelector("[data-flash-title]");
    const p = box.querySelector("[data-flash-detail]");

    box.classList.remove("hidden");
    pill.className = "pill " + (type || "warn");
    pill.textContent = (type || "info").toUpperCase();

    if (h) h.textContent = title || "";
    if (p) p.textContent = detail || "";
  }

  function clearFlash() {
    const box = document.getElementById("flash");
    if (!box) return;
    box.classList.add("hidden");
  }

  function pick(obj, keys, fallback = "") {
    for (const k of keys) {
      if (obj && Object.prototype.hasOwnProperty.call(obj, k) && obj[k] !== null && obj[k] !== undefined) return obj[k];
    }
    return fallback;
  }

  function normalizeList(data) {
    if (Array.isArray(data)) return data;
    if (data && Array.isArray(data.items)) return data.items;
    if (data && Array.isArray(data.results)) return data.results;
    return [];
  }

  window.DC_UI = { setFlash, clearFlash, pick, normalizeList };
})();
