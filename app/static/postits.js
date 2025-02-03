document.addEventListener("DOMContentLoaded", function() {

    // Ajouter un nouveau post-it
    document.getElementById("add-postit").addEventListener("click", function() {
        fetch("/api/postits/new", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ titre: "Nouveau Post-it", contenu: "Écrivez ici..." })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === "Post-it créé avec succès") {
                location.reload(); // Recharge la page après ajout
            } else {
                alert("Erreur lors de la création du Post-it");
            }
        });
    });

    // Modifier un post-it en sauvegardant automatiquement
    document.querySelectorAll(".editable").forEach(element => {
        element.addEventListener("blur", function() {
            sauvegarderPostit(this);
        });

        // Sauvegarde avec la touche "Entrée"
        element.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
                this.blur(); // Simule la perte de focus pour sauvegarder
            }
        });
    });

    function sauvegarderPostit(element) {
        let postit = element.closest(".postit");
        let postitId = postit.getAttribute("data-id");
        let titre = postit.querySelector(".titre").value.trim();
        let contenu = postit.querySelector(".contenu").value.trim();

        fetch(`/api/postits/${postitId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ titre: titre, contenu: contenu })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message !== "Post-it mis à jour avec succès") {
                alert("Erreur lors de la mise à jour !");
            }
        });
    }

    // Supprimer un post-it
    document.querySelectorAll(".supprimer-postit").forEach(button => {
        button.addEventListener("click", function() {
            let postit = this.closest(".postit");
            let postitId = postit.getAttribute("data-id");

            if (confirm("Voulez-vous vraiment supprimer ce post-it ?")) {
                fetch(`/api/postits/${postitId}`, { method: "DELETE" })
                .then(response => response.json())
                .then(data => {
                    if (data.message === "Post-it supprimé avec succès") {
                        postit.remove(); // Supprime l'élément sans recharger la page
                    } else {
                        alert("Erreur lors de la suppression !");
                    }
                });
            }
        });
    });
    function reorganiserPostits() {
        let postitContainer = document.querySelector("#postits-container");
        
        if (postitContainer) {
            let postits = Array.from(postitContainer.children);
            postits.sort((a, b) => {
                let dateA = new Date(a.getAttribute("data-created-at"));
                let dateB = new Date(b.getAttribute("data-created-at"));
                return dateA - dateB; // Trie les post-its par date de création
            });
    
            postitContainer.innerHTML = ""; // Vide le conteneur
            postits.forEach(postit => postitContainer.appendChild(postit)); // Réinsère les post-its triés
        }
    }
});
