# Utilisation d'une image Python légère
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    postgresql-client \
 && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires pour l'installation des dépendances
COPY requirements.txt .

# Installation des dépendances Python avec `--no-cache-dir` pour éviter d'alourdir l'image
RUN pip install --no-cache-dir -r requirements.txt

# Création d'un utilisateur non root
RUN useradd -m myuser

# Copier le reste du code de l'application
COPY . .

# Assurer les permissions sur le dossier migrations
RUN mkdir -p /app/migrations && chown -R myuser:myuser /app/migrations

# Définition des variables d'environnement
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Exposition du port Flask
EXPOSE 5000

# Passer en utilisateur non root
USER myuser

# Commande de démarrage (avec entrypoint pour init migrations)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]
