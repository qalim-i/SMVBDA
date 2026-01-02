const btn = document.getElementById("langToggle");
const currentPath = window.location.pathname;

// Set correct button text
if (currentPath.includes("kannada")) {
  btn.textContent = "English";
} else {
  btn.textContent = "Kannada";
}

// Handle page switch
btn.addEventListener("click", () => {
  if (currentPath.includes("kannada")) {
    window.location.href = "/";
  } else {
    window.location.href = "/kannada/";
  }
});

// Tab Switching Logic
document.addEventListener('DOMContentLoaded', () => {
  const tabs = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.tab-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.target;

      // Update Tabs
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      // Update Panels
      panels.forEach(panel => {
        panel.classList.remove('active');
        if (panel.id === target) {
          panel.classList.add('active');
        }
      });
    });
  });

  // Mobile Menu Toggle
  const mobileBtn = document.querySelector('.mobile-menu-btn');
  const nav = document.querySelector('.main-nav');
  const navLinks = document.querySelectorAll('.main-nav a');

  console.log('Mobile Menu Elements:', { mobileBtn, nav }); // Debugging

  if (mobileBtn && nav) {
    mobileBtn.addEventListener('click', (e) => {
      e.stopPropagation(); // Prevent bubbling issues
      console.log('Mobile menu clicked'); // Debugging
      mobileBtn.classList.toggle('active');
      nav.classList.toggle('active');
      document.body.classList.toggle('no-scroll'); // Optional: prevent body scroll
    });

    // Close menu when link is clicked
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileBtn.classList.remove('active');
        nav.classList.remove('active');
        document.body.classList.remove('no-scroll');
      });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target) && !mobileBtn.contains(e.target) && nav.classList.contains('active')) {
        nav.classList.remove('active');
        mobileBtn.classList.remove('active');
        document.body.classList.remove('no-scroll');
      }
    });

  }
});
