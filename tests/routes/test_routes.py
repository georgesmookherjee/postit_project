def test_ping_db(client):
    """
    Teste la connexion à la base de données via la route /ping_db.
    """
    response = client.get('/ping_db')
    assert response.status_code == 200
    assert response.json['message'] == "Connexion à la base de données réussie"
