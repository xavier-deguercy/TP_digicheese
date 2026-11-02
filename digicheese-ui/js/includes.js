document.addEventListener("DOMContentLoaded", async () => {
  const nodes = document.querySelectorAll("[data-include]");

  await Promise.all([...nodes].map(async (el) => {
    const url = el.getAttribute("data-include");
    if (!url) return;

    const resp = await fetch(url, { cache: "no-store" });
    if (!resp.ok) {
      console.error("[include] échec", url, resp.status);
      return;
    }

    el.innerHTML = await resp.text();
    el.removeAttribute("data-include");
  }));

  const currentPage = window.location.pathname.split("/").pop() || "dashboard.html";
  document.querySelectorAll('.nav a[href]:not([data-action="logout"])').forEach((link) => {
    const active = link.getAttribute("href") === currentPage;
    link.classList.toggle("active", active);
    if (active) link.setAttribute("aria-current", "page");
    else link.removeAttribute("aria-current");
  });
});

document.addEventListener("click", (event) => {
  const logout = event.target.closest('[data-action="logout"]');
  if (logout && window.DC_API) window.DC_API.clearStoredAuthValue();

  const teamButton = event.target.closest("#btnTeam");
  if (!teamButton) return;
  const panel = document.getElementById("teamPanel");
  if (!panel) return;
  const isOpen = teamButton.getAttribute("aria-expanded") === "true";
  teamButton.setAttribute("aria-expanded", String(!isOpen));
  panel.hidden = isOpen;
});
