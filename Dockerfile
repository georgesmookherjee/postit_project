# Utilisation de l'image Python 3.12 (version stable disponible)
FROM python:3.13-slim

# Installation de toutes les dépendances système en une seule étape
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    wget \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    xdg-utils \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Définition du répertoire de travail
WORKDIR /app

# Copie du fichier de dépendances et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer Playwright et ses navigateurs
RUN pip install playwright pytest-playwright && \
    playwright install chromium --with-deps

# Installation de Blackfire
RUN pip install --no-cache-dir blackfire

# Copie du code source
COPY . .

# Exposition du port utilisé par Flask
EXPOSE 5000

# Commande de démarrage
# CMD ["python", "run.py", "--host=0.0.0.0", "--port=5000", "--reload"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]