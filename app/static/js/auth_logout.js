document.addEventListener("DOMContentLoaded", () => {
    const logoutBtn = document.getElementById("logout-btn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", () => {
            fetch("/auth/logout", {
                method: "POST",
                credentials: "include"
            })
            .then(() => window.location.href = "/");
        });
    }
});
