document.addEventListener("DOMContentLoaded", function() { 

    // Modifier un post-it en sauvegardant automatiquement
    document.querySelectorAll(".editable").forEach(element => {
        element.addEventListener("blur", function() {
            sauvegarderPostit(this);
        });

        // Sauvegarde avec la touche "Entrée"
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
});
