// Initialize all functionality when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Theme toggle functionality
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    
    // Check for saved theme preference
    if (localStorage.getItem('theme') === 'dark' || 
        (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        html.classList.add('dark');
    } else {
        html.classList.remove('dark');
    }

    // Toggle theme
    themeToggle.addEventListener('click', function() {
        html.classList.toggle('dark');
        localStorage.setItem('theme', html.classList.contains('dark') ? 'dark' : 'light');
    });

    // Mobile menu functionality
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!mobileMenu.contains(event.target) && !mobileMenuButton.contains(event.target)) {
                mobileMenu.classList.add('hidden');
            }
        });

        // Close mobile menu when clicking a link
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // Initialize AOS
    AOS.init({
        duration: 800,
        once: true
    });

    // Initialize Swiper for each skills category
    const swipers = document.querySelectorAll('.swiper');
    swipers.forEach((swiper, index) => {
        new Swiper(swiper, {
            slidesPerView: 1,
            spaceBetween: 20,
            loop: true,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                },
                768: {
                    slidesPerView: 3,
                },
                1024: {
                    slidesPerView: 4,
                },
            },
        });
    });

    // Initialize infinite scroll with alternating directions
    const skillsTracks = document.querySelectorAll('.skills-track');
    
    skillsTracks.forEach((track, index) => {
        // Clone the first set of skills
        const skills = Array.from(track.children);
        skills.forEach(skill => {
            const clone = skill.cloneNode(true);
            track.appendChild(clone);
        });

        // Reset animation when it ends
        track.addEventListener('animationend', () => {
            track.style.animation = 'none';
            track.offsetHeight; // Trigger reflow
            track.style.animation = index % 2 === 0 ? 'scrollLeft 30s linear infinite' : 'scrollRight 30s linear infinite';
        });
    });

    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const form = e.target;
            const submitButton = form.querySelector('button[type="submit"]');
            const formMessage = document.getElementById('formMessage');
            
            // Disable submit button and show loading state
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="flex items-center justify-center gap-2"><i class="fas fa-spinner fa-spin"></i> Sending...</span>';
            
            try {
                const response = await fetch('/send-email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        name: form.name.value,
                        email: form.email.value,
                        message: form.message.value
                    })
                });
                
                const data = await response.json();
                
                // Show success/error message
                formMessage.classList.remove('hidden');
                if (data.status === 'success') {
                    formMessage.classList.add('bg-green-100', 'text-green-800', 'dark:bg-green-900/30', 'dark:text-green-300');
                    formMessage.innerHTML = '<i class="fas fa-check-circle mr-2"></i> Message sent successfully!';
                    form.reset();
                } else {
                    formMessage.classList.add('bg-red-100', 'text-red-800', 'dark:bg-red-900/30', 'dark:text-red-300');
                    formMessage.innerHTML = '<i class="fas fa-exclamation-circle mr-2"></i> Failed to send message. Please try again.';
                }
            } catch (error) {
                formMessage.classList.remove('hidden');
                formMessage.classList.add('bg-red-100', 'text-red-800', 'dark:bg-red-900/30', 'dark:text-red-300');
                formMessage.innerHTML = '<i class="fas fa-exclamation-circle mr-2"></i> An error occurred. Please try again.';
            } finally {
                // Re-enable submit button and restore original text
                submitButton.disabled = false;
                submitButton.innerHTML = '<span class="flex items-center justify-center gap-2"><i class="fas fa-paper-plane"></i> Send Message</span>';
            }
        });
    }
});