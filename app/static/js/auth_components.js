// app/static/js/auth_components.js
function createAuthForm(containerId, onSuccessRedirect = null) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    // Injecter le HTML du formulaire
    container.innerHTML = `
        <div class="card p-4 shadow">
            <h3 class="text-center mb-4">Connexion</h3>
            <div class="mb-3">
                <label for="email" class="form-label">Email :</label>
                <input type="email" id="email" class="form-control" placeholder="Votre email" required>
            </div>
            <div class="mb-3">
                <label for="username" class="form-label">Nom d'utilisateur :</label>
                <input type="text" id="username" class="form-control" placeholder="Nom d'utilisateur">
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Mot de passe :</label>
                <input type="password" id="password" class="form-control" placeholder="Votre mot de passe" required>
            </div>
            <button type="button" id="login-btn" class="btn btn-primary w-100">Se connecter</button>
            <button type="button" id="register-btn" class="btn btn-secondary w-100 mt-2">Créer un compte</button>
        </div>
    `;
    
    // Attacher les événements
    const loginBtn = document.getElementById("login-btn");
    const registerBtn = document.getElementById("register-btn");
    
    loginBtn.addEventListener("click", () => handleLogin(onSuccessRedirect));
    registerBtn.addEventListener("click", () => handleRegister(onSuccessRedirect));
}

function handleLogin(redirectUrl = null) {
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
            showNotification(data.message);
            if (redirectUrl) {
                window.location.href = redirectUrl;
            } else {
                window.location.reload();
            }
        } else if (data.error) {
            showNotification("Erreur : " + data.error);
        }
    })
    .catch(err => {
        console.error("Erreur serveur :", err);
        showNotification("Erreur de connexion");
    });
}

function handleRegister(redirectUrl = null) {
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
            if (redirectUrl) {
                window.location.href = redirectUrl;
            } else {
                window.location.reload();
            }
        } else if (data.error) {
            showNotification("Erreur : " + data.error);
        }
    })
    .catch(err => {
        console.error("Erreur serveur :", err);
        showNotification("Erreur lors de l'inscription");
    });
}