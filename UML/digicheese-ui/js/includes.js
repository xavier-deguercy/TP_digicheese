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
});
