
    function toggleMenu() {
      const menu = document.querySelector('.profile-menu');
      menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    }

    // Close the profile menu if clicked outside
    window.addEventListener('click', function(event) {
      const menu = document.querySelector('.profile-menu');
      const profileAvatar = document.querySelector('.profile-avatar');
      if (!profileAvatar.contains(event.target)) {
        menu.style.display = 'none';
      }
    });

    function toggleMobileNav() {
      const mobileNav = document.querySelector('.mobile-nav-links');
      mobileNav.classList.toggle('show');
    }
