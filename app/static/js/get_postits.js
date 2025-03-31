// get_postits.js
document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("postit-container");
    if (container) {
        chargerPostIts();
    }
});

async function chargerPostIts() {
    try {
        const res = await fetch("/api/postits");
        
        if (!res.ok) {
            if (res.status === 401) {
                document.getElementById("postit-container").innerHTML = 
                    "<p class='text-center'>Veuillez vous connecter pour voir vos post-its</p>";
                return;
            }
            throw new Error(`Erreur HTTP ${res.status}`);
        }
        
        const data = await res.json();
        afficherPostIts(data);
    } catch (error) {
        console.warn("Erreur contrôlée:", error.message);
        showNotification("Impossible de charger les post-its");
    }
}
