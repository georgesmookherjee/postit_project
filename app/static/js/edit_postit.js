document.addEventListener("input", function(event) {
    if (event.target.classList.contains("editable")) {
        sauvegarderPostit(event.target);
    }
});

document.addEventListener("keypress", function(event) {
    if (event.target.classList.contains("editable") && event.key === "Enter") {
        if (event.shiftKey) {
            event.preventDefault();
            event.target.value += "\n"; // Ajoute un saut de ligne
        } else {
            event.preventDefault();
            event.target.blur(); // Simule la perte de focus pour sauvegarder
        }
    }
});
