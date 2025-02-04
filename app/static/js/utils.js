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
