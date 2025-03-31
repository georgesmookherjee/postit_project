// postit_events.js
document.addEventListener("DOMContentLoaded", function() {
    // Initialisation centrale des événements
    initPostItEvents();
});

// Fonction principale d'initialisation
function initPostItEvents() {
    // Vérifie si on est sur une page avec des post-its
    const container = document.getElementById("postit-container");
    if (!container) return;
    
    // Initialisation du bouton d'ajout
    initAddButton();
    
    // Initialisation des événements sur les post-its existants
    attachEventListeners();
}

// Initialise le bouton d'ajout
function initAddButton() {
    let addButton = document.getElementById("add-postit");
    if (addButton) {
        addButton.addEventListener("click", ajouterPostit);
    }
}

// Ajoute un nouveau post-it
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

// Attache tous les événements aux post-its
function attachEventListeners() {
    // Gestion des boutons de modification
    attachEditEvents();
    
    // Gestion des champs éditables
    attachEditableEvents();
    
    // Gestion des boutons de suppression
    attachDeleteEvents();
}

// Gestion des événements de modification
function attachEditEvents() {
    document.querySelectorAll(".modifier-postit").forEach(button => {
        button.addEventListener("click", function() {
            sauvegarderPostit(this.closest(".postit"));
        });
    });
}

// Gestion des événements pour les champs éditables
function attachEditableEvents() {
    document.querySelectorAll(".editable").forEach(element => {
        // Sauvegarde en quittant le champ
        element.addEventListener("blur", function() {
            sauvegarderPostit(this.closest(".postit"));
        });
        
        // Sauvegarde avec Entrée ou ajout de saut de ligne avec Shift+Entrée
        element.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                if (event.shiftKey) {
                    event.preventDefault();
                    this.value += "\n"; // Ajoute un saut de ligne
                } else {
                    event.preventDefault();
                    this.blur(); // Simule la perte de focus pour sauvegarder
                }
            }
        });
    });
}

// Gestion des événements de suppression
function attachDeleteEvents() {
    document.querySelectorAll(".supprimer-postit").forEach(button => {
        button.addEventListener("click", function() {
            let postit = this.closest(".postit");
            let postitId = postit.getAttribute("data-id");

            fetch(`/api/postits/${postitId}`, { method: "DELETE" })
            .then(response => response.json())
            .then(data => {
                if (data.message === "Post-it supprimé avec succès") {
                    postit.closest(".col-md-4").remove(); // Suppression du DOM sans rechargement
                    showNotification("Post-it supprimé");
                } else {
                    showNotification("Erreur lors de la suppression !");
                }
            })
            .catch(error => {
                showNotification("Erreur lors de la communication avec le serveur");
                console.error(error);
            });
        });
    });
}