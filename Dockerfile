# Utiliser une image Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "run.py"]