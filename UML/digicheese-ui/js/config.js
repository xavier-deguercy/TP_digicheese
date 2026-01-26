/**
 * Digicheese Admin UI — Configuration
 * Ajuste API_BASE et l'auth (X-API-Key) selon ton environnement.
 */
window.DC_CONFIG = {
  API_BASE: "http://127.0.0.1:8000",

  // Auth actuelle de Digicheese : API Key via header "X-API-Key"
  AUTH: {
    enabled: true,
    scheme: "api_key",               // "api_key" (Digicheese) | "bearer"
    headerName: "X-API-Key",
    storageKey: "dc_api_key",

    // Dév : si tu lances l'API avec DISABLE_AUTH=true, tu peux mettre enabled=false
    // enabled: false,
  },

  ENDPOINTS: {
    health: "/health",
    objets: "/objets",
    conditionnements: "/conditionnements"
  },

  // Mapping des noms de champs côté API
  FIELDS: {
    objet: {
      id: "id_objet",
      lib: "nom_obj",
      taille: "taille_obj",
      prix: "prix_obj"
    },
    conditionnement: {
      id: "id_condit",
      lib: "lib_condit",
      poids: "poids_condit",
      prix: "prix_condit",
      ordre: "ordre_imp"
    }
  }
};
