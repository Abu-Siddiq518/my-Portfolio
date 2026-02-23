// ===========================
// CYBER PORTFOLIO - MAIN JS
// ===========================

document.addEventListener('DOMContentLoaded', function () {

  // ===========================
  // MATRIX RAIN EFFECT
  // ===========================
  const canvas = document.getElementById('matrix-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()[]{}|<>?/\\~';
    const fontSize = 14;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = new Array(columns).fill(1);

    function drawMatrix() {
      ctx.fillStyle = 'rgba(5, 5, 16, 0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.fillStyle = '#00ff41';
      ctx.font = `${fontSize}px Share Tech Mono, monospace`;

      for (let i = 0; i < drops.length; i++) {
        const char = chars[Math.floor(Math.random() * chars.length)];
        const x = i * fontSize;
        const y = drops[i] * fontSize;

        // Vary brightness for depth effect
        if (drops[i] * fontSize < 50) {
          ctx.fillStyle = '#ffffff';
        } else if (Math.random() > 0.9) {
          ctx.fillStyle = '#00ffcc';
        } else {
          ctx.fillStyle = '#00ff41';
        }

        ctx.fillText(char, x, y);

        if (y > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }
        drops[i]++;
      }
    }

    setInterval(drawMatrix, 50);

    window.addEventListener('resize', () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    });
  }

  // ===========================
  // TYPING EFFECT
  // ===========================
  const typedEl = document.getElementById('typed');
  if (typedEl) {
    const phrases = [
      'Abubakkar Siddiq A',
      'Penetration Tester',
      'Ethical Hacker',
      'VAPT Specialist',
      'Security Researcher',
      'CTF Player',
    ];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function type() {
      const currentPhrase = phrases[phraseIndex];

      if (isDeleting) {
        typedEl.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
      } else {
        typedEl.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
      }

      let delay = isDeleting ? 60 : 100;

      if (!isDeleting && charIndex === currentPhrase.length) {
        delay = 2000;
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        delay = 500;
      }

      setTimeout(type, delay);
    }

    setTimeout(type, 1000);
  }

  // ===========================
  // NAVBAR SCROLL EFFECT
  // ===========================
  const navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  }

  // ===========================
  // SMOOTH ACTIVE NAV LINKS
  // ===========================
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      if (window.scrollY >= sectionTop) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // ===========================
  // HAMBURGER MENU
  // ===========================
  const hamburger = document.getElementById('hamburger');
  const navLinksList = document.querySelector('.nav-links');

  if (hamburger && navLinksList) {
    hamburger.addEventListener('click', () => {
      navLinksList.classList.toggle('open');
    });

    navLinksList.addEventListener('click', () => {
      navLinksList.classList.remove('open');
    });
  }

  // ===========================
  // COUNTER ANIMATION
  // ===========================
  function animateCount(el, target, duration = 2000) {
    let start = 0;
    const step = target / (duration / 16);
    const timer = setInterval(() => {
      start += step;
      if (start >= target) {
        el.textContent = target;
        clearInterval(timer);
      } else {
        el.textContent = Math.floor(start);
      }
    }, 16);
  }

  const counters = document.querySelectorAll('.stat-num[data-count]');
  let countersStarted = false;

  function startCounters() {
    if (countersStarted) return;
    counters.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-count'));
      animateCount(counter, target);
    });
    countersStarted = true;
  }

  // ===========================
  // INTERSECTION OBSERVER
  // ===========================
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');

        // Trigger skill progress bars
        if (entry.target.classList.contains('skill-card')) {
          const bar = entry.target.querySelector('.skill-progress');
          if (bar) {
            const pcts = [92, 88, 90, 85, 80, 78, 85, 82];
            const cards = document.querySelectorAll('.skill-card');
            const idx = Array.from(cards).indexOf(entry.target);
            setTimeout(() => {
              bar.style.width = (pcts[idx % pcts.length]) + '%';
            }, 200);
          }
        }

        // Trigger stat counters when hero stats are visible
        if (entry.target.classList.contains('hero-stats')) {
          startCounters();
        }
      }
    });
  }, observerOptions);

  // Observe elements
  document.querySelectorAll('.skill-card, .project-card, .cert-card, .ach-card, .timeline-card, .edu-card, .hero-stats').forEach(el => {
    observer.observe(el);
    el.classList.add('fade-up');
  });

  // ===========================
  // CSS ANIMATION HELPERS
  // ===========================
  const style = document.createElement('style');
  style.textContent = `
    .fade-up {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.6s ease, transform 0.6s ease;
    }
    .fade-up.visible {
      opacity: 1;
      transform: translateY(0);
    }
    .nav-link.active {
      color: var(--green) !important;
      background: rgba(0, 255, 65, 0.08) !important;
      border-color: rgba(0, 255, 65, 0.3) !important;
    }
  `;
  document.head.appendChild(style);

  // ===========================
  // CONTACT FORM — AJAX SUBMIT
  // ===========================
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = document.getElementById('sendBtn');
      const feedback = document.getElementById('form-feedback');
      const original = btn.innerHTML;

      btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> TRANSMITTING...';
      btn.disabled = true;

      const formData = new FormData(contactForm);

      fetch('/contact', { method: 'POST', body: formData })
        .then(r => r.json())
        .then(data => {
          feedback.style.display = 'block';
          if (data.status === 'ok') {
            feedback.style.cssText = 'display:block;padding:.8rem 1rem;margin-bottom:1rem;border-radius:6px;font-family:var(--font-mono);font-size:.85rem;background:rgba(0,255,65,.1);border:1px solid var(--green);color:var(--green);';
            feedback.innerHTML = '✅ ' + data.msg;
            contactForm.reset();
          } else {
            feedback.style.cssText = 'display:block;padding:.8rem 1rem;margin-bottom:1rem;border-radius:6px;font-family:var(--font-mono);font-size:.85rem;background:rgba(255,0,64,.1);border:1px solid #ff0040;color:#ff0040;';
            feedback.innerHTML = '⚠️ ' + data.msg;
          }
          setTimeout(() => { feedback.style.display = 'none'; }, 5000);
        })
        .catch(() => {
          feedback.style.cssText = 'display:block;padding:.8rem 1rem;border-radius:6px;font-family:var(--font-mono);font-size:.85rem;background:rgba(255,0,64,.1);border:1px solid #ff0040;color:#ff0040;';
          feedback.innerHTML = '⚠️ Network error. Please try again.';
        })
        .finally(() => {
          btn.innerHTML = original;
          btn.disabled = false;
        });
    });
  }

  // ===========================
  // PARALLAX HERO GRID
  // ===========================
  const heroGrid = document.querySelector('.hero-grid');
  if (heroGrid) {
    window.addEventListener('scroll', () => {
      const offset = window.scrollY * 0.3;
      heroGrid.style.transform = `translateY(${offset}px)`;
    });
  }

  // ===========================
  // GLITCH ON HOVER
  // ===========================
  const glitchText = document.querySelector('.glitch-text');
  if (glitchText) {
    glitchText.addEventListener('mouseenter', () => {
      glitchText.style.animation = 'glitch 0.3s infinite';
    });
    glitchText.addEventListener('mouseleave', () => {
      glitchText.style.animation = 'glitch 4s infinite';
    });
  }

  // ===========================
  // CURSOR TRAIL EFFECT
  // ===========================
  let mouseX = 0, mouseY = 0;
  const trails = [];

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    createTrail(e.clientX, e.clientY);
  });

  function createTrail(x, y) {
    const trail = document.createElement('div');
    trail.style.cssText = `
      position: fixed;
      width: 4px;
      height: 4px;
      background: #00ff41;
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      top: ${y}px;
      left: ${x}px;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 6px #00ff41;
      animation: trailFade 0.5s ease forwards;
    `;
    document.body.appendChild(trail);
    setTimeout(() => trail.remove(), 500);
  }

  // Add trail fade animation
  const trailStyle = document.createElement('style');
  trailStyle.textContent = `
    @keyframes trailFade {
      0% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
      100% { opacity: 0; transform: translate(-50%, -50%) scale(0.1); }
    }
  `;
  document.head.appendChild(trailStyle);

  // ===========================
  // TERMINAL TYPEWRITER FOR ABOUT
  // ===========================
  function typewriter(element, text, speed = 30) {
    let i = 0;
    element.innerHTML = '';
    const timer = setInterval(() => {
      if (i < text.length) {
        element.innerHTML += text.charAt(i);
        i++;
      } else {
        clearInterval(timer);
      }
    }, speed);
  }

  // ===========================
  // RANDOM HEX BACKGROUND
  // ===========================
  function generateHexBg() {
    const hexChars = '0123456789ABCDEF';
    let result = '#';
    for (let i = 0; i < 6; i++) {
      result += hexChars[Math.floor(Math.random() * 16)];
    }
    return result;
  }

  // Background data stream in footer
  const footerMatrix = document.querySelector('.footer-matrix');
  if (footerMatrix) {
    let stream = '';
    for (let i = 0; i < 500; i++) {
      stream += Math.random() > 0.5 ? '1' : '0';
      if (i % 50 === 0) stream += ' ';
    }
    footerMatrix.style.cssText = `
      position: absolute;
      inset: 0;
      font-family: 'Share Tech Mono', monospace;
      font-size: 10px;
      color: rgba(0, 255, 65, 0.04);
      overflow: hidden;
      word-break: break-all;
      padding: 1rem;
      pointer-events: none;
    `;
    footerMatrix.textContent = stream;
  }

  console.log(`
  ██████╗██╗   ██╗██████╗ ███████╗██████╗     ██████╗  ██████╗ ██████╗ ████████╗███████╗ ██████╗ ██╗     ██╗ ██████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔═══██╗██║     ██║██╔═══██╗
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██║   ██║██║     ██║██║   ██║
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██║   ██║██║     ██║██║   ██║
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ██║     ╚██████╔╝██║  ██║   ██║   ██║     ╚██████╔╝███████╗██║╚██████╔╝
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝

  🔐 Abubakkar Siddiq A | Cybersecurity Professional
  💡 Ethical Hacking | VAPT | Penetration Testing
  `);
});
