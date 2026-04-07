/* ============================================
   CREATE ALLIED HEALTH — Interactive Scripts
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    /* ─────────────────────────────────────────
       1. NAV SCROLL EFFECT
       ───────────────────────────────────────── */
    const nav = document.getElementById('nav');

    if (nav) {
        const onScroll = () => {
            if (window.scrollY > 60) {
                nav.classList.add('nav--scrolled');
            } else {
                nav.classList.remove('nav--scrolled');
            }
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    /* ─────────────────────────────────────────
       2. MOBILE NAV TOGGLE
       ───────────────────────────────────────── */
    const navToggle = document.getElementById('navToggle');
    const navLinks  = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('nav__links--open');
            navToggle.classList.toggle('nav__toggle--open', isOpen);
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });

        // Close mobile nav when any link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                // Don't close if it's a dropdown trigger on mobile
                if (link.classList.contains('nav__dropdown-trigger') && window.innerWidth < 1024) {
                    return;
                }
                navToggle.classList.remove('nav__toggle--open');
                navLinks.classList.remove('nav__links--open');
                document.body.style.overflow = '';
            });
        });
    }

    /* ─────────────────────────────────────────
       3. DROPDOWN MENUS
       ───────────────────────────────────────── */
    const dropdowns = document.querySelectorAll('.nav__dropdown');

    dropdowns.forEach(dropdown => {
        const trigger = dropdown.querySelector('.nav__dropdown-trigger');
        const menu    = dropdown.querySelector('.nav__dropdown-menu');
        if (!trigger || !menu) return;

        // Mobile: toggle dropdown on click
        trigger.addEventListener('click', (e) => {
            if (window.innerWidth < 1024) {
                e.preventDefault();
                e.stopPropagation();

                // Close other open dropdowns
                dropdowns.forEach(other => {
                    if (other !== dropdown) {
                        other.classList.remove('nav__dropdown--open');
                    }
                });

                dropdown.classList.toggle('nav__dropdown--open');
            }
        });

        // Desktop: show/hide on hover
        dropdown.addEventListener('mouseenter', () => {
            if (window.innerWidth >= 1024) {
                dropdown.classList.add('nav__dropdown--open');
            }
        });

        dropdown.addEventListener('mouseleave', () => {
            if (window.innerWidth >= 1024) {
                dropdown.classList.remove('nav__dropdown--open');
            }
        });
    });

    /* ─────────────────────────────────────────
       4. SERVICE TABS (homepage only)
       ───────────────────────────────────────── */
    const tabs   = document.querySelectorAll('.services__tab');
    const panels = document.querySelectorAll('.services__panel');

    if (tabs.length && panels.length) {
        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const target = tab.dataset.tab;

                tabs.forEach(t => t.classList.remove('services__tab--active'));
                tab.classList.add('services__tab--active');

                panels.forEach(p => p.classList.remove('services__panel--active'));
                const targetPanel = document.getElementById(`panel-${target}`);
                if (targetPanel) {
                    targetPanel.classList.add('services__panel--active');
                }
            });
        });
    }

    /* ─────────────────────────────────────────
       5. SCROLL REVEAL
       ───────────────────────────────────────── */
    const revealSelectors = [
        '.pillar',
        '.service-card',
        '.partner-card',
        '.about__image-wrapper',
        '.about__content',
        '.values__card',
        '.value-card',
        '.job-card',
        '.blog-card',
        '.package-card',
        '.contact__info',
        '.contact__form-wrapper',
        '.cta-band__inner',
        '.service-detail__sidebar',
        '.service-detail__content',
        '.team-member',
        '.hiring-card',
        '.team-profile__image-wrapper',
        '.team-profile__content',
        '.story-content',
        '.benefit-card',
        '.testimonial-card'
    ];

    const revealElements = document.querySelectorAll(revealSelectors.join(', '));

    revealElements.forEach(el => {
        el.classList.add('reveal');
    });

    if (revealElements.length) {
        const revealed = new Set();

        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (!entry.isIntersecting || revealed.has(entry.target)) return;

                // Find siblings with .reveal in the same parent
                const parent   = entry.target.parentElement;
                const siblings = Array.from(parent.querySelectorAll(':scope > .reveal'));
                let delay = 0;

                siblings.forEach(sib => {
                    if (!revealed.has(sib) && sib.getBoundingClientRect().top < window.innerHeight) {
                        revealed.add(sib);
                        setTimeout(() => {
                            sib.classList.add('reveal--visible');
                        }, delay);
                        delay += 80;
                        revealObserver.unobserve(sib);
                    }
                });

                // Ensure the entry target itself is revealed
                if (!revealed.has(entry.target)) {
                    revealed.add(entry.target);
                    entry.target.classList.add('reveal--visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.05,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));
    }

    /* ─────────────────────────────────────────
       6. SMOOTH ANCHOR SCROLL
       ───────────────────────────────────────── */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const href = anchor.getAttribute('href');
            if (href === '#') return; // skip bare "#" links (dropdown triggers)

            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    /* ─────────────────────────────────────────
       7. CONTACT / REFERRAL FORM HANDLING
       ───────────────────────────────────────── */
    const forms = document.querySelectorAll('#contactForm, #referralForm');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const btn = form.querySelector('button[type="submit"]');
            if (!btn) return;

            const originalText = btn.textContent;
            const originalBg   = btn.style.background;

            btn.textContent = 'Sending...';
            btn.disabled    = true;

            // Simulate send (replace with actual form handler in production)
            setTimeout(() => {
                btn.textContent      = "Sent! We'll be in touch.";
                btn.style.background = 'var(--sage)';

                setTimeout(() => {
                    btn.textContent      = originalText;
                    btn.style.background = originalBg;
                    btn.disabled         = false;
                    form.reset();
                }, 3000);
            }, 1200);
        });
    });

    /* ─────────────────────────────────────────
       8. HERO PARALLAX (homepage only)
       ───────────────────────────────────────── */
    const heroImg = document.querySelector('.hero__img');

    if (heroImg) {
        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const scrolled = window.scrollY;
                    if (scrolled < window.innerHeight) {
                        heroImg.style.transform = `scale(1.05) translateY(${scrolled * 0.15}px)`;
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    /* ─────────────────────────────────────────
       9. ACTIVE NAV LINK
       ───────────────────────────────────────── */
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';

    if (navLinks) {
        navLinks.querySelectorAll('a').forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPage) {
                link.classList.add('nav__link--active');
            }
        });
    }

    /* ─────────────────────────────────────────
       10. SIDEBAR ACTIVE LINK (service detail pages)
       ───────────────────────────────────────── */
    const sidebar = document.querySelector('.service-detail__sidebar');

    if (sidebar) {
        sidebar.querySelectorAll('a').forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPage) {
                link.classList.add('active');
            }
        });
    }

});
