from bs4 import BeautifulSoup

def test_admin_panel_requires_admin(authenticated_client):
    """Teste que le panneau d'admin est accessible uniquement aux administrateurs."""
    # Essayer d'accéder sans être connecté
    response = authenticated_client.get('/admin')
    assert response.status_code == 403  # Forbidden
    
    # Créer un utilisateur normal
    authenticated_client.post('/auth/register', json={
        'username': 'normaluser',
        'email': 'normal@example.com',
        'password': 'normalpass'
    })
    
    # Se connecter en tant qu'utilisateur normal
    authenticated_client.post('/auth/login', json={
        'identifier': 'normal@example.com',
        'password': 'normalpass'
    })
    
    # Essayer d'accéder au panneau d'administration
    response = authenticated_client.get('/admin')
    assert response.status_code == 403  # Forbidden

def test_admin_panel_content(client):
    """Teste le contenu du panneau d'administration."""
    from app.models import User, db
    
    # Créer un utilisateur admin
    admin_user = User(username='adminview', email='adminview@example.com')
    admin_user.set_password('adminpass')
    admin_user.is_admin = True
    db.session.add(admin_user)
    db.session.commit()
    
    # Connecter l'admin
    client.post('/auth/login', json={
        'identifier': 'adminview@example.com',
        'password': 'adminpass'
    })
    
    # Accéder au panneau d'admin
    response = client.get('/admin')
    assert response.status_code == 200
    
    # Analyser le contenu HTML
    soup = BeautifulSoup(response.data, 'html.parser')
    
    # Vérifier les éléments essentiels
    assert soup.select('div#stats-container')
    assert soup.select('div#users-list')