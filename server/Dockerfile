# Image de base officielle Python 3.12 slim (bookworm)
FROM python:3.12.0-slim-bookworm

# Variables d'environnement pour éviter le buffering et les fichiers pyc
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement requirements.txt en premier (pour profiter du cache Docker)
COPY requirements.txt /app/

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copier tout le reste du code dans le répertoire de travail
COPY . /app/

# Exposer le port 8000 (celui que Django/Gunicorn utilisera)
EXPOSE 8000

# Si tu as un script d'entrée, rends-le exécutable (si tu en as un)
RUN chmod +x /app/entrypoint.sh

# Définir l'entrypoint pour lancer ton script bash (optionnel, si tu l'as)
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Commande par défaut pour démarrer Gunicorn (ton serveur WSGI)
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
