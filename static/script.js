document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-current-year]").forEach(el => el.textContent = new Date().getFullYear());
  document.querySelectorAll("a[href^='#']").forEach(link => {
    link.addEventListener("click", () => {
      const target = document.querySelector(link.getAttribute("href"));
      if (target) target.scrollIntoView({behavior:"smooth", block:"start"});
    });
  });
});
