document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("auth-form");
    const registerBtn = document.getElementById("register-btn");

    if (registerBtn) {
        registerBtn.addEventListener("click", function (e) {
            e.preventDefault();

            const email = document.getElementById("email").value;
            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            fetch("/auth/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email, username, password })
            })
            .then(res => res.json())
            .then(data => {
                if (data.message) {
                    showNotification(data.message);
                    location.reload();
                } else if (data.error) {
                    showNotification("Erreur : " + data.error);
                }
            })
            .catch(err => {
                console.error("Erreur serveur :", err);
                showNotification(data.message);
            });
        });
    }
});