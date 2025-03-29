document.addEventListener("DOMContentLoaded", function () {
    fetch("/auth/status")
        .then(res => res.json())
        .then(data => {
            const welcomeUser = document.getElementById("welcome-user");
            const logoutBtn = document.getElementById("logout-btn");

            if (data.logged_in) {
                if (logoutBtn) logoutBtn.style.display = "inline";
                if (welcomeUser) welcomeUser.textContent = `Bonjour ${data.username} !`;
            } else {
                if (logoutBtn) logoutBtn.style.display = "none";
                if (welcomeUser) welcomeUser.textContent = `Bonjour Visiteur !`;
            }
        })
        .catch(err => {
            console.error("Erreur de statut d'authentification :", err);
        });
});
