/* Digicheese Admin UI — API helper (API Key / Bearer) */
(function () {
  const cfg = window.DC_CONFIG;

  function getStoredAuthValue() {
    try { return localStorage.getItem(cfg.AUTH.storageKey) || ""; }
    catch { return ""; }
  }

  function setStoredAuthValue(v) {
    try { localStorage.setItem(cfg.AUTH.storageKey, v || ""); } catch {}
  }

  function clearStoredAuthValue() {
    try { localStorage.removeItem(cfg.AUTH.storageKey); } catch {}
  }

  function joinUrl(base, path) {
    const b = base.replace(/\/$/, "");
    const p = (path || "").startsWith("/") ? path : "/" + (path || "");
    return b + p;
  }

  async function apiFetch(path, options = {}) {
    const url = joinUrl(cfg.API_BASE, path);
    const headers = new Headers(options.headers || {});

    // JSON par défaut si body est objet
    if (options.body && typeof options.body === "object" && !(options.body instanceof FormData)) {
      headers.set("Content-Type", "application/json");
      options.body = JSON.stringify(options.body);
    }

    // Auth
    if (cfg.AUTH && cfg.AUTH.enabled) {
      const v = getStoredAuthValue();
      if (v) {
        if (cfg.AUTH.scheme === "api_key") {
          headers.set(cfg.AUTH.headerName || "X-API-Key", v);
        } else if (cfg.AUTH.scheme === "bearer") {
          headers.set("Authorization", "Bearer " + v);
        }
      }
    }

    const resp = await fetch(url, { ...options, headers });

    const ct = resp.headers.get("content-type") || "";
    let data = null;
    if (ct.includes("application/json")) {
      try { data = await resp.json(); } catch { data = null; }
    } else {
      try { data = await resp.text(); } catch { data = null; }
    }

    if (!resp.ok) {
      const err = new Error("HTTP " + resp.status);
      err.status = resp.status;
      err.data = data;
      throw err;
    }
    return data;
  }

  // Pour Digicheese (API key), "login" = enregistrer la clé.
  async function login(apiKey) {
    if (!cfg.AUTH.enabled) return "";
    setStoredAuthValue(apiKey || "");
    return apiKey || "";
  }

  window.DC_API = {
    apiFetch,
    login,
    getStoredAuthValue,
    setStoredAuthValue,
    clearStoredAuthValue
  };
})();
