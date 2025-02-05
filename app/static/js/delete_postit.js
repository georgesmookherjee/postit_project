document.addEventListener("DOMContentLoaded", function() {

    // Supprimer un post-it
    document.querySelectorAll(".supprimer-postit").forEach(button => {
        button.addEventListener("click", function() {
            let postit = this.closest(".postit");
            let postitId = postit.getAttribute("data-id");

            fetch(`/api/postits/${postitId}`, { method: "DELETE" })
            .then(response => response.json())
            .then(data => {
                if (data.message === "Post-it supprimé avec succès") {
                    postit.remove(); // Supprime l'élément sans recharger la page
                    location.reload(); // Recharge la page après la suppression
                } else {
                    alert("Erreur lors de la suppression !");
                }
            });
        });
    });
});
