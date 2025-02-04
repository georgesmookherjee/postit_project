document.addEventListener("click", function(event) {
    if (event.target.classList.contains("supprimer-postit")) {
        let postit = event.target.closest(".postit");
        let postitId = postit.getAttribute("data-id");

        if (confirm("Voulez-vous vraiment supprimer ce post-it ?")) {
            fetch(`/api/postits/${postitId}`, { method: "DELETE" })
            .then(response => response.json())
            .then(data => {
                if (data.message === "Post-it supprimé avec succès") {
                    postit.remove(); // Supprime immédiatement
                } else {
                    alert("Erreur lors de la suppression !");
                }
            });
        }
    }
});
