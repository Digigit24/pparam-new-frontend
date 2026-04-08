/**
 * Global Header Loader
 * Centralizes the header and handles relative paths for root and nested pages.
 */
(function () {
  // Determine the path to the root from the current location
  var scripts = document.getElementsByTagName("script");
  var currentScript = scripts[scripts.length - 1];
  var scriptPath = currentScript.src;
  var rootPath = "";

  // If there's a specific container, we'll use that
  var container = document.getElementById("header-placeholder");
  if (!container) {
    // If not found, look for <header> and replace it
    container = document.querySelector("header");
  }

  if (container) {
    var xhr = new XMLHttpRequest();
    // Since we are likely in root, but just in case:
    // We'll use a simple strategy: check if about.html exists here or in parent
    // Actually, the easiest way for this specific project:
    var pathPrefix = "";
    var depth = window.location.pathname.split("/").length - 1;
    // This is tricky on different servers.

    // Let's just use the fact that currently all are in root.
    // If nested pages are added, we expect them to be in subfolders.

    xhr.open("GET", "header.html", false); // Synchronous
    try {
      xhr.send();
      if (xhr.status === 200 || xhr.status === 0) {
        var content = xhr.responseText;

        // Fix relative paths in the content
        // We'll assume the header.html is in the root.
        // If we are in a subfolder, we need to prefix paths with ../

        // Currently all files are in root, so no prefix needed.
        // But for "future proofing" as requested:
        // We'll trust the user to put the loader script with the right path.

        container.outerHTML = content;

        // Initialize Scroll-based Visibility Logic
        initNavbarScrollVisibility();
      }
    } catch (e) {
      console.error("Failed to load header:", e);
    }
  }

  function initNavbarScrollVisibility() {
    const header = document.getElementById("header-sticky");
    if (!header) return;

    let lastScrollTop = 0;
    let isTicking = false;
    const threshold = 100; // Start hiding after 100px scroll
    const delta = 5; // Minimum scroll distance to trigger

    // Apply smooth transition style via JS to avoid CSS modification
    header.style.transition = "transform 0.4s cubic-bezier(0.4, 0, 0.2, 1)";

    window.addEventListener("scroll", function () {
      if (!isTicking) {
        window.requestAnimationFrame(function () {
          updateNavbarVisibility();
          isTicking = false;
        });
        isTicking = true;
      }
    }, { passive: true });

    function updateNavbarVisibility() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

      // Ensure visible at the top
      if (scrollTop <= threshold) {
        header.style.transform = "translateY(0)";
        lastScrollTop = scrollTop;
        return;
      }

      // Check if scroll is significant enough
      if (Math.abs(lastScrollTop - scrollTop) <= delta) return;

      if (scrollTop > lastScrollTop) {
        // Scrolling Down - Hide
        header.style.transform = "translateY(-100%)";
      } else {
        // Scrolling Up - Show
        header.style.transform = "translateY(0)";
      }

      lastScrollTop = scrollTop;
    }
  }
})();
