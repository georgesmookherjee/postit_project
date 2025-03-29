document.addEventListener("DOMContentLoaded", function () {
    const loginBtn = document.getElementById("login-btn");

    if (loginBtn) {
        loginBtn.addEventListener("click", function (e) {
            e.preventDefault();

            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            fetch("/auth/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ identifier: email, password })
            })
            .then(res => res.json())
            .then(data => {
                if (data.message) {
                    location.reload();
                } else if (data.error) {
                    alert("Erreur : " + data.error);
                }
            })
            .catch(err => {
                console.error("Erreur serveur :", err);
                alert("Erreur de connexion");
            });
        });
    }
});
