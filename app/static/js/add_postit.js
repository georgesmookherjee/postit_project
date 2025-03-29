document.addEventListener("DOMContentLoaded", function () {
    let addButton = document.getElementById("add-postit");
    if (!addButton) {
        console.error("⚠️ Bouton d'ajout non trouvé !");
        return;
    }

    addButton.addEventListener("click", ajouterPostit);
});

function ajouterPostit() {
    fetch("/api/postits", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titre: " ", contenu: " " })
    })
    .then(response => response.ok ? response.json() : Promise.reject(response.status))
    .then(data => afficherPostit(data))
    .catch(error => {
        console.error("Erreur lors de la requête :", error);
        showNotification("Erreur serveur. Vérifiez votre connexion.");
    });
}

function afficherPostit(data) {
    if (!data.id) {
        alert("Erreur lors de la création du Post-it");
        return;
    }

    let postitContainer = document.getElementById("postit-container");
    let newPostit = document.createElement("div");
    newPostit.classList.add("col-md-4");
    newPostit.innerHTML = `
        <div class="card postit p-3 mb-3" data-id="${data.id}">
            <input type="text" class="postit-title editable titre" value="${data.titre}" />
            <textarea class="postit-content editable contenu form-control mt-2">${data.contenu}</textarea>
            <small class="text-muted">Créé le : ${data.date_creation}</small>
            <div class="d-flex justify-content-between mt-2">
                <button class="btn btn-outline-primary modifier-postit">Modifier</button>
                <button class="btn btn-outline-danger supprimer-postit">Supprimer</button>
            </div>
        </div>
    `;
    postitContainer.appendChild(newPostit);
    location.reload();
}
