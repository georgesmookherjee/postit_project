// app/static/js/admin.js
document.addEventListener('DOMContentLoaded', function() {
    fetchStats();
    fetchUsers();
});

async function fetchStats() {
    try {
        const response = await fetch('/admin/api/stats');
        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }
        const stats = await response.json();
        
        document.getElementById('users-count').textContent = stats.users_total;
        document.getElementById('postits-count').textContent = stats.postits_total;
        document.getElementById('avg-postits').textContent = stats.avg_postits_per_user;
    } catch (error) {
        console.error('Erreur:', error);
        showNotification('Erreur lors du chargement des statistiques');
    }
}

async function fetchUsers() {
    try {
        const response = await fetch('/admin/api/users');
        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }
        const users = await response.json();
        displayUsers(users);
    } catch (error) {
        console.error('Erreur:', error);
        showNotification('Erreur lors du chargement des utilisateurs');
    }
}

function displayUsers(users) {
    const container = document.getElementById('users-list');
    
    if (!users || users.length === 0) {
        container.innerHTML = '<p class="text-center">Aucun utilisateur trouvé</p>';
        return;
    }
    
    let html = `
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nom d'utilisateur</th>
                    <th>Email</th>
                    <th>Statut</th>
                    <th>Post-its</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
    `;
    
    users.forEach(user => {
        html += `
            <tr>
                <td>${user.id}</td>
                <td>${user.username}</td>
                <td>${user.email}</td>
                <td>
                    <span class="badge ${user.is_admin ? 'bg-danger' : 'bg-secondary'}">
                        ${user.is_admin ? 'Admin' : 'Utilisateur'}
                    </span>
                </td>
                <td>${user.postits_count}</td>
                <td>
                    ${!user.is_admin ? 
                        `<button class="btn btn-sm btn-outline-primary make-admin" data-id="${user.id}">
                            Promouvoir admin
                        </button>` : 
                        `<button class="btn btn-sm btn-outline-danger revoke-admin" data-id="${user.id}">
                            Révoquer admin
                        </button>`
                    }
                </td>
            </tr>
        `;
    });
    
    html += `
            </tbody>
        </table>
    `;
    
    container.innerHTML = html;
    
    // Attacher les événements
    document.querySelectorAll('.make-admin').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-id');
            makeAdmin(userId);
        });
    });
    
    document.querySelectorAll('.revoke-admin').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-id');
            revokeAdmin(userId);
        });
    });
}

async function makeAdmin(userId) {
    try {
        const response = await fetch(`/admin/api/users/${userId}/make-admin`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }
        
        const data = await response.json();
        showNotification(data.message);
        fetchUsers(); // Recharger la liste
    } catch (error) {
        console.error('Erreur:', error);
        showNotification("Erreur lors de la modification du statut d'administrateur");
    }
}

async function revokeAdmin(userId) {
    try {
        const response = await fetch(`/admin/api/users/${userId}/revoke-admin`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.ok) {
            const data = await response.json();
            showNotification(data.error || "Erreur lors de la révocation des droits");
            return;
        }
        
        const data = await response.json();
        showNotification(data.message);
        fetchUsers(); // Recharger la liste
    } catch (error) {
        console.error('Erreur:', error);
        showNotification("Erreur lors de la modification du statut d'administrateur");
    }
}