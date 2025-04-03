from flask.testing import FlaskClient

def test_register_user(client: FlaskClient):
    """Teste l'enregistrement d'un nouvel utilisateur."""
    response = client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 201
    assert 'message' in response.json
    assert response.json['message'] == 'Inscription réussie'

def test_login_success(client: FlaskClient):
    """Teste la connexion d'un utilisateur."""
    # D'abord créer un utilisateur
    client.post('/auth/register', json={
        'username': 'logintest',
        'email': 'login@example.com',
        'password': 'password123'
    })
    
    # Essayer de se connecter
    response = client.post('/auth/login', json={
        'identifier': 'login@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'Connexion réussie'

def test_admin_api_access(client: FlaskClient):
    """Teste l'accès aux API d'administration."""
    from app.models import User, db
    
    # Créer un utilisateur administrateur
    admin_user = User(username='admin', email='admin@example.com')
    admin_user.set_password('adminpass')
    admin_user.is_admin = True
    db.session.add(admin_user)
    db.session.commit()
    
    # Connecter l'administrateur
    client.post('/auth/login', json={
        'identifier': 'admin@example.com',
        'password': 'adminpass'
    })
    
    # Tester l'accès à une API d'administration
    response = client.get('/admin/api/stats')
    assert response.status_code == 200
    assert 'users_total' in response.json

