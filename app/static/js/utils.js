
function sauvegarderPostit(element) {
    let postit = element.closest(".postit");
    let postitId = postit.getAttribute("data-id");
    let titre = postit.querySelector(".titre").value.trim();
    let contenu = postit.querySelector(".contenu").value.trim();

    return fetch(`/api/postits/${postitId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titre: titre, contenu: contenu })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erreur HTTP ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.message === "Post-it mis à jour avec succès") {
            showNotification("Post-it sauvegardé !");
            return data;
        } else {
            throw new Error("Erreur lors de la mise à jour");
        }
    })
    .catch(error => {
        showNotification("Erreur : " + error.message);
        throw error;
    });
}

function showNotification(message, duration = 3000) {
    const box = document.getElementById("message-box");
    box.textContent = message;
    box.classList.add("show");
    box.classList.remove("hide");
  
    setTimeout(() => {
      box.classList.add("hide");
      box.classList.remove("show");
    }, duration);
  }

// Dans utils.js
function afficherPostIts(data) {
    const container = document.getElementById("postit-container");
    container.innerHTML = "";

    if (!data || data.length === 0) {
        container.innerHTML = "<p class='text-center'>Aucun post-it trouvé</p>";
        return;
    }

    data.forEach(postit => {
        afficherPostit(postit, false); // Le second paramètre indique de ne pas attacher les événements immédiatement
    });
    
    // Attacher les événements une seule fois après avoir ajouté tous les post-its
    attachEventListeners();
}

function afficherPostit(data, attachEvents = true) {
    if (!data.id) {
        showNotification("Erreur: données de post-it invalides");
        return;
    }

    let postitContainer = document.getElementById("postit-container");
    let newPostit = document.createElement("div");
    newPostit.classList.add("col-md-4");
    newPostit.innerHTML = `
        <div class="card postit p-3 mb-3" data-id="${data.id}">
            <input type="text" class="postit-title editable titre" value="${data.titre}" />
            <textarea class="postit-content editable contenu form-control mt-2">${data.contenu}</textarea>
            <small class="text-muted">Créé le : ${formatDate(data.created_at || data.date_creation)}</small>
            <div class="d-flex justify-content-between mt-2">
                <button class="btn btn-outline-success modifier-postit">ok</button>
                <button class="btn btn-outline-danger supprimer-postit">Supprimer</button>
            </div>
        </div>
    `;
    postitContainer.appendChild(newPostit);
    
    // Attacher les événements si demandé (par exemple lors de l'ajout d'un seul post-it)
    if (attachEvents) {
        attachEventListeners();
    }
}

// Assurez-vous que formatDate est aussi dans utils.js
function formatDate(dateStr) {
    if (!dateStr || dateStr === "null") return "Date inconnue";
    
    // Remplacer " " par "T" pour un format ISO valide
    let isoDateStr = typeof dateStr === 'string' ? dateStr.replace(" ", "T") : dateStr;
    
    let date = new Date(isoDateStr);
    if (isNaN(date.getTime())) return "Date inconnue";
    
    return date.toLocaleString("fr-FR", { 
        year: "numeric", 
        month: "2-digit", 
        day: "2-digit", 
        hour: "2-digit", 
        minute: "2-digit", 
        hour12: false
    }).replace(",", "");
}