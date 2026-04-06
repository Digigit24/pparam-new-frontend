/**
 * Global Footer Loader
 * Centralizes the footer and handles relative paths for root and nested pages.
 */
(function() {
    // 1. Identify the container
    var container = document.getElementById("global-footer");
    if (!container) {
        // Fallback: look for <footer> and replace it if possible
        container = document.querySelector("footer");
    }

    if (!container) return;

    // 2. Determine path to root
    // We can use the script tag's src property to find where it's located
    var scripts = document.getElementsByTagName("script");
    var currentScript = null;
    for (var i = 0; i < scripts.length; i++) {
        if (scripts[i].src.indexOf("footer-loader.js") !== -1) {
            currentScript = scripts[i];
            break;
        }
    }

    var rootPath = "";
    if (currentScript) {
        var scriptSrc = currentScript.getAttribute("src");
        // If scriptSrc is "assets/js/footer-loader.js", we are in root (0 levels up)
        // If scriptSrc is "../assets/js/footer-loader.js", we are 1 level deep
        var match = scriptSrc.match(/^(\.\.\/)+/);
        if (match) {
            rootPath = match[0];
        }
    }

    // 3. Fetch the footer.html
    var xhr = new XMLHttpRequest();
    xhr.open("GET", rootPath + "footer.html", false); // Synchronous to avoid layout shift
    try {
        xhr.send();
        if (xhr.status === 200 || xhr.status === 0) {
            var content = xhr.responseText;

            // 4. Update relative paths in content if we are in a subfolder
            if (rootPath !== "") {
                // Correct for images, links, and background URLs starting with assets/
                content = content.replace(/(src|href|data-background)=["'](assets\/[^"']+)["']/g, '$1="' + rootPath + '$2"');
                
                // Correct for inline styles url(assets/...)
                content = content.replace(/url\(assets\/([^)]+)\)/g, 'url(' + rootPath + 'assets/$1)');
                
                // Correct relative HTML links (e.g. index.html, contact.html)
                // But don't touch absolute links like https:// or mailto: or #
                content = content.replace(/href=["'](?!\w+:\/\/|#|mailto:)([^"']+\.html)["']/g, 'href="' + rootPath + '$1"');
            }

            // 5. Inject the content
            // We replace the placeholder with the actual content
            container.outerHTML = content;

            // 6. Handle the dynamic year if needed (the footer has <span id="year"></span>)
            var yearSpan = document.getElementById("year");
            if (yearSpan) {
                yearSpan.textContent = new Date().getFullYear();
            }
        }
    } catch (e) {
        console.error("Failed to load footer:", e);
    }
})();
