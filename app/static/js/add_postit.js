document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("add-postit").addEventListener("click", function() {
        fetch("/api/postits/new", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ titre: "nouveau", contenu: "..." })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Réponse complète du serveur :", data); // Debugging
            if (data.message === "Post-it créé avec succès") {
                let postitContainer = document.getElementById("postit-container");
                let newPostit = document.createElement("div");
                newPostit.classList.add("col-md-4");
                newPostit.innerHTML = `
                    <div class="card postit p-3 mb-3" data-id="${data.post_it}">
                        <input type="text" class="postit-title editable titre" value="${data.postit.titre}" />
                        <textarea class="postit-content editable contenu form-control mt-2">${data.postit.contenu}</textarea>
                        <small class="text-muted">Créé le : ${data.postit.date_creation}</small>
                        <div class="d-flex justify-content-between mt-2">
                            <button class="btn btn-outline-primary modifier-postit">Modifier</button>
                            <button class="btn btn-outline-danger supprimer-postit">Supprimer</button>
                        </div>
                    </div>
                `;
                postitContainer.appendChild(newPostit); // Ajoute à la fin
                location.reload(); // Recharge la page pour éviter tout problème
            } else {
                alert("Erreur lors de la création du Post-it");
            }
        });
    });
});
