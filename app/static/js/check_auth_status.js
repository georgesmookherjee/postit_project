document.addEventListener("DOMContentLoaded", function () {
    fetch("/auth/status")
        .then(res => {
            //console.log("Réponse API /auth/status :", res);
            if (!res.ok) {
                if (res.status === 401) {
                    return { logged_in: false };
                }
                throw new Error(`Erreur HTTP ${res.status}`);
            }
            return res.json();
        })
        .then(data => {
            const welcomeUser = document.getElementById("welcome-user");
            const logoutBtn = document.getElementById("logout-btn");
            const authForm = document.getElementById("auth-form");

            if (data.logged_in) {
                logoutBtn?.style && (logoutBtn.style.display = "inline");
                authForm?.style && (authForm.style.display = "none");

                if (welcomeUser) {
                    welcomeUser.textContent = `Bonjour ${data.username}`;

                    // Crée le lien vers les post-its
                    const link = document.createElement("a");
                    link.href = "/postits";
                    link.className = "btn btn-outline-primary mt-1"; 
                    link.textContent = "Accéder à vos post-its";
                    link.id = "btn-access-postits"

                    // Ajoute le lien sous le message de bienvenue
                    welcomeUser.insertAdjacentElement("afterend", link);
                }
            } else {
                logoutBtn?.style && (logoutBtn.style.display = "none");
                authForm?.style && (authForm.style.display = "block");
                if (welcomeUser) welcomeUser.textContent = `Bonjour Visiteur !`;
            }
        })
        .catch(err => {
            console.warn("utilisateur non connecté ou problème réseau");
        });
});
