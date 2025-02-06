# Utiliser une image Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

RUN apt-get update && apt-get install -y postgresql-client

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "run.py"]

# Ajouter un utilisateur non-root et lui attribuer un home directory
RUN useradd -m myuser

# Changer les permissions du dossier de travail pour cet utilisateur
RUN chown -R myuser:myuser /app

# Passer en mode utilisateur non-root
USER myuser

# Définition de la variable d'environnement indiquant le fichier principal de l'application Flask
ENV FLASK_APP=run.py
# Flask saura que le fichier d'entrée est run.py

# Définition du mode d'exécution de Flask (développement ou production)
ENV FLASK_ENV=development  
#Active le mode développement (permet le rechargement auto et le debug)
