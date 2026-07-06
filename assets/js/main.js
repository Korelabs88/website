// Año dinámico en el footer
const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();

// Marquee — JS en desktop (Chrome bloquea CSS animation con backdrop-filter en la página)
(function initMarquee() {
  const track = document.querySelector(".marquee__track");
  if (!track || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  track.classList.add("is-js");
  track.style.animation = "none";

  let offset = 0;
  let half = 0;
  let last = performance.now();
  const speed = 55; // px/s

  const measure = () => {
    half = track.scrollWidth / 2;
  };
  measure();
  if ("ResizeObserver" in window) {
    new ResizeObserver(measure).observe(track);
  } else {
    window.addEventListener("resize", measure, { passive: true });
  }

  function tick(now) {
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    if (half > 0) {
      offset += speed * dt;
      if (offset >= half) offset -= half;
      track.style.transform = `translate3d(${-offset}px, 0, 0)`;
    }
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();

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

// Selector de idioma: cerrar al hacer clic fuera
document.addEventListener("click", (e) => {
  document.querySelectorAll("details.lang-dropdown[open]").forEach((dropdown) => {
    if (!dropdown.contains(e.target)) dropdown.open = false;
  });
});

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

// Fondo tipo Matrix (azul neón)
(function matrixRain() {
  const canvas = document.getElementById("matrix");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  // Katakana (estilo Matrix) + algunos dígitos
  const chars =
    "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン0123456789".split("");

  let cols = [];
  let w = 0;
  let h = 0;

  function build() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
    const gap = 13; // separación base menor que el tamaño => se superponen
    const count = Math.ceil(w / gap);
    cols = [];
    for (let i = 0; i < count; i++) {
      const size = 11 + Math.random() * 20; // 11..31: disonancia de tamaños
      cols.push({
        x: i * gap + (Math.random() * 6 - 3),
        size: size,
        y: Math.random() * -h,
        speed: size * 0.38 + Math.random() * 2.2, // más grande = más rápido (profundidad)
        alpha: 0.26 + (size / 31) * 0.74,          // más grande = más brillante
      });
    }
  }
  build();
  window.addEventListener("resize", build, { passive: true });

  function palette() {
    const dark = document.documentElement.getAttribute("data-theme") === "dark";
    return dark
      ? { fade: "rgba(11, 13, 21, 0.11)", tail: "#2E6BFF", head: "#CFE0FF" }
      : { fade: "rgba(246, 247, 251, 0.16)", tail: "#3E6BFF", head: "#1B45E0" };
  }

  const fps = 30;
  const interval = 1000 / fps;
  let lastTime = 0;

  function draw(now) {
    requestAnimationFrame(draw);
    if (now - lastTime < interval) return;
    lastTime = now;

    const c = palette();
    ctx.fillStyle = c.fade;
    ctx.fillRect(0, 0, w, h);
    ctx.textBaseline = "top";

    for (let k = 0; k < cols.length; k++) {
      const col = cols[k];
      const ch = chars[(Math.random() * chars.length) | 0];
      ctx.font = col.size + "px 'Courier New', monospace";

      if (Math.random() > 0.93) {
        // cabeza brillante con destello
        ctx.globalAlpha = 1;
        ctx.shadowColor = c.head;
        ctx.shadowBlur = col.size * 0.9;
        ctx.fillStyle = c.head;
      } else {
        ctx.globalAlpha = col.alpha;
        ctx.shadowBlur = 0;
        ctx.fillStyle = c.tail;
      }
      ctx.fillText(ch, col.x, col.y);

      col.y += col.speed;
      if (col.y > h + col.size && Math.random() > 0.96) {
        col.y = Math.random() * -140;
      }
    }
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
  }
  requestAnimationFrame(draw);
})();

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

// Botón flotante Ko-fi: aparece al hacer scroll y anima la taza
const kofiFloat = document.getElementById("kofiFloat");
if (kofiFloat && !reduceMotion) {
  let scrollTimer;
  let lastY = window.scrollY;
  const showAfter = 180;

  const onKofiScroll = () => {
    const y = window.scrollY;
    kofiFloat.classList.toggle("is-visible", y > showAfter);

    if (Math.abs(y - lastY) > 2) {
      kofiFloat.classList.add("is-scrolling");
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => kofiFloat.classList.remove("is-scrolling"), 200);
    }
    lastY = y;
  };

  onKofiScroll();
  window.addEventListener("scroll", onKofiScroll, { passive: true });
} else if (kofiFloat) {
  kofiFloat.classList.add("is-visible");
}

// Modal de contacto
const contactModal = document.getElementById("contactModal");
const contactForm = document.getElementById("contactForm");
const contactStatus = document.getElementById("contactStatus");
let contactTrigger = null;

function openContactModal(trigger) {
  if (!contactModal) return;
  contactTrigger = trigger || null;
  contactModal.hidden = false;
  contactModal.setAttribute("aria-hidden", "false");
  requestAnimationFrame(() => contactModal.classList.add("is-open"));
  document.body.style.overflow = "hidden";
  const first = contactForm?.querySelector("input:not(.contact-form__hp)");
  first?.focus();
}

function closeContactModal() {
  if (!contactModal) return;
  contactModal.classList.remove("is-open");
  contactModal.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
  window.setTimeout(() => {
    if (!contactModal.classList.contains("is-open")) contactModal.hidden = true;
  }, 280);
  contactTrigger?.focus();
  contactTrigger = null;
}

document.querySelectorAll("[data-contact-open]").forEach((btn) => {
  btn.addEventListener("click", () => openContactModal(btn));
});

contactModal?.querySelectorAll("[data-contact-close]").forEach((el) => {
  el.addEventListener("click", closeContactModal);
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && contactModal?.classList.contains("is-open")) {
    e.preventDefault();
    closeContactModal();
  }
});

if (contactForm) {
  const msgSending = contactForm.dataset.msgSending || "Sending…";
  const msgSuccess = contactForm.dataset.msgSuccess || "Sent!";
  const msgError = contactForm.dataset.msgError || "Error sending.";

  contactForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const submitBtn = contactForm.querySelector(".contact-form__submit");
    const payload = {
      name: contactForm.querySelector("#contactName").value.trim(),
      email: contactForm.querySelector("#contactEmail").value.trim(),
      message: contactForm.querySelector("#contactMessage").value.trim(),
      website: contactForm.website.value,
    };

    if (!payload.name || !payload.email || !payload.message) {
      contactStatus.textContent = msgError;
      contactStatus.className = "contact-form__status is-error";
      return;
    }

    submitBtn.disabled = true;
    contactStatus.textContent = msgSending;
    contactStatus.className = "contact-form__status";

    try {
      const res = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!res.ok) throw new Error("fail");
      contactStatus.textContent = msgSuccess;
      contactStatus.className = "contact-form__status is-success";
      contactForm.reset();
      window.setTimeout(closeContactModal, 2200);
    } catch {
      contactStatus.textContent = msgError;
      contactStatus.className = "contact-form__status is-error";
    } finally {
      submitBtn.disabled = false;
    }
  });
}
