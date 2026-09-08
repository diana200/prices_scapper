// DARK MODE TOGGLE
document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("darkModeToggle");

    if (toggle) {
        toggle.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");

            // Save preference
            const isDark = document.body.classList.contains("dark-mode");
            localStorage.setItem("darkMode", isDark ? "1" : "0");
        });
    }

    // Load preference
    if (localStorage.getItem("darkMode") === "1") {
        document.body.classList.add("dark-mode");
    }
});
