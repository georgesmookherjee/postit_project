# Projet Post-It

## Description
Ce projet est une application web permettant de créer, modifier et supprimer des post-its. Il repose sur Flask pour le backend, PostgreSQL pour la base de données et utilise Docker pour la gestion des environnements. C'est un projet que je réalise dans le cadre de l'apprentissage de la programmation Back-end.

## Prérequis
- **Docker** et **Docker Compose** installés
- **Python 3.12+**
- **pipenv** pour la gestion des dépendances (optionnel si utilisation avec Docker)

## Installation et mise en route
### 1. Cloner le projet
```bash
git clone https://github.com/georgesmookherjee/postit_project.git
cd postit_project
```
### 2. Configuration de l'environnement
Créer un fichier `.env` à la racine du projet en se basant sur `.env.example`.

Modifier les variables en fonction de l'environnement (développement ou test) :
```bash
APP_ENV=development  # Ou "testing" pour exécuter les tests
DEV_DATABASE_URL=postgresql://user:password@post_it_db:5432/post_it
TEST_DATABASE_URL=postgresql://user:password@post_it_test_db:5432/test_post_it
```
### 3. Lancer l'application avec Docker
```bash
docker-compose up --build -d
```
Vérifier que les conteneurs sont bien démarrés :
```bash
docker ps
```
L'application sera accessible sur `http://localhost:5000`.

## Exécution des tests
Pour exécuter les tests avec Docker :
```bash
docker-compose exec flask_app python -m pytest -v
```
Pour exécuter un test spécifique :
```bash
docker-compose exec flask_app python -m pytest -v tests/api/test_postits_api.py::test_create_postit
```
En cas de problème avec la base de données de test, vider les volumes avec :
```bash
docker-compose down
```
Puis relancer les conteneurs :
```bash
docker-compose up --build -d
```

## Déploiement
Une fois les tests validés, on peut déployer l'application.
1. **Construire l'image pour le déploiement**
   ```bash
   docker build -t postit_app_prod .
   ```
2. **Pousser l'image sur un registre (Docker Hub, AWS, etc.)**
   ```bash
   docker tag postit_app_prod username/postit_app_prod
   docker push username/postit_app_prod
   ```
3. **Configurer l'hébergement** (Render, DigitalOcean, Railway...)
   - Adapter les variables d'environnement.
   - Configurer les bases de données distantes.
   - Déployer l'image.



## Améliorations futures
- Séparation complète backend / frontend avec React
- Ajouter "Automatisation des tests et CI/CD" si tu envisages d'intégrer une pipeline GitHub Actions ou autre.

## Auteur
- **Georges Mookherjee** - [GitHub](https://github.com/georgesmookherjee)

