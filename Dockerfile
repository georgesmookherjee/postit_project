# Utilisation de l'image Python légère
FROM python:3.12-slim

# Installation des dépendances système requises (si PostgreSQL est utilisé)
RUN apt-get update && apt-get install -y libpq-dev postgresql-client && rm -rf /var/lib/apt/lists/*

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier de dépendances et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Exposition du port utilisé par Flask
EXPOSE 5000

# Commande de démarrage
CMD ["python", "run.py"]
