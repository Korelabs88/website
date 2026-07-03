// Año dinámico en el footer
const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();

// Modo oscuro / claro
const root = document.documentElement;
const themeToggle = document.getElementById("themeToggle");
const themeMeta = document.querySelector('meta[name="theme-color"]');

function applyThemeColor(theme) {
  if (themeMeta) themeMeta.setAttribute("content", theme === "dark" ? "#0B0D15" : "#F6F7FB");
}
applyThemeColor(root.getAttribute("data-theme"));

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    applyThemeColor(next);
    try {
      localStorage.setItem("theme", next);
    } catch (e) {}
  });
}

// Sombra sutil del nav al hacer scroll
const nav = document.querySelector(".nav");
if (nav) {
  const onScroll = () => {
    nav.style.boxShadow = window.scrollY > 8 ? "0 6px 24px rgba(22, 23, 27, 0.06)" : "none";
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

// Reveal on scroll (respetando prefers-reduced-motion)
const reveals = document.querySelectorAll("[data-reveal]");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (reduceMotion || !("IntersectionObserver" in window)) {
  reveals.forEach((el) => el.classList.add("is-in"));
} else {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
  );

  // Stagger sutil entre elementos hermanos
  let last = null;
  let step = 0;
  reveals.forEach((el) => {
    const parent = el.parentElement;
    step = parent === last ? step + 1 : 0;
    last = parent;
    el.style.setProperty("--d", Math.min(step, 5) * 70 + "ms");
    io.observe(el);
  });
}
