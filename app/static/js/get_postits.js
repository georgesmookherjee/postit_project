document.addEventListener("DOMContentLoaded", function() {
    // fetch("/auth/status")
    //     .then(response => response.json())
    //     .then(data => {
    //         if (!data.logged_in) {
    //             alert("Vous devez être connecté pour accéder à cette page.");
    //             return;
    //         }
    //         document.getElementById("auth-links").innerHTML = `
    //             <a href="/auth/logout" id="logout-link">Se déconnecter (${data.username})</a>
    //         `;
            chargerPostIts();
        });
//});

function chargerPostIts() {
    fetch("/api/postits")
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("postit-container");
            container.innerHTML = "";

            if (data.length === 0) {
                container.innerHTML = "<p class='text-center'>Aucun post-it trouvé.</p>";
                return;
            }

            data.forEach(postit => {
                const postitDiv = document.createElement("div");
                postitDiv.className = "col-md-4";
                postitDiv.innerHTML = `
                    <div class="card postit p-3 mb-3" data-id="${postit.id}">
                        <input type="text" class="postit-title editable titre" maxlength="25" value="${postit.titre}"/>
                        <textarea class="postit-content editable contenu form-control mt-2">${postit.contenu}</textarea>              
                        <small class="text-muted">Créé le : ${formatDate(postit.created_at)}</small>
                        <div class="d-flex justify-content-between mt-2">
                            <button class="btn btn-outline-success modifier-postit">ok</button>
                            <button class="btn btn-outline-danger supprimer-postit"> Supprimer </button>
                        </div>
                    </div>
                `;
                container.appendChild(postitDiv);
            });

            attachEventListeners();
        })
        .catch(error => console.error("Erreur lors de la récupération des post-its:", error));
}

// Fonction pour formater la date correctement
function formatDate(dateStr) {
    if (!dateStr || dateStr === "null") return "Date inconnue";

    // Remplacer " " par "T" pour un format ISO valide
    let isoDateStr = dateStr.replace(" ", "T");

    let date = new Date(isoDateStr);
    if (isNaN(date.getTime())) return "Date inconnue";  // Vérification de validité

    // Format anglais "YYYY-MM-DD HH:MM"
    return date.toLocaleString("en-GB", { 
        year: "numeric", 
        month: "2-digit", 
        day: "2-digit", 
        hour: "2-digit", 
        minute: "2-digit", 
        hour12: false // Format 24h (pas AM/PM)
    }).replace(",", ""); // Supprime la virgule ajoutée par défaut
}

// Fonction pour réactiver les événements de modification et suppression après le chargement
function attachEventListeners() {
    document.querySelectorAll(".modifier-postit").forEach(button => {
        button.addEventListener("click", function() {
            sauvegarderPostit(this.closest(".postit"));
        });
    });

    document.querySelectorAll(".editable").forEach(element => {
        // Sauvegarder en appuyant sur "Entrée"
        element.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                if (event.shiftKey) {
                    event.preventDefault();
                    this.value += "\n"; // Ajoute un saut de ligne si Shift + Entrée
                } else {
                    event.preventDefault();
                    this.blur(); // Simule la perte de focus pour sauvegarder
                    sauvegarderPostit(this.closest(".postit"));
                }
            }
        });

        // Sauvegarder aussi en perdant le focus
        element.addEventListener("blur", function() {
            sauvegarderPostit(this.closest(".postit"));
        });
    });

    document.querySelectorAll(".supprimer-postit").forEach(button => {
        button.addEventListener("click", function() {
            let postit = this.closest(".postit");
            let postitId = postit.getAttribute("data-id");

            fetch(`/api/postits/${postitId}`, { method: "DELETE" })
            .then(response => response.json())
            .then(data => {
                if (data.message === "Post-it supprimé avec succès") {
                    location.reload(); // Recharge la page après suppression
                } else {
                    alert("Erreur lors de la suppression !");
                }
            });
        });
    });
}