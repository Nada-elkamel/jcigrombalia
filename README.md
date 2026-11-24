# Site Web Officiel — JCI Grombalia (Version 100% Django + Turso + Render)

Projet institutionnel complet développé avec **Python**, **Django**, **Django REST Framework**, **Django Templates (HTML5 + Bootstrap 5)**, **Turso (libSQL)** en production (ou SQLite en local) et prêt pour l'hébergement sur **Render**.

## Architecture modulaire

- `core` : page d'accueil, paramètres généraux, tableau de bord administrateur et médiathèque.
- `accounts` : authentification administrateur unique (inscription publique désactivée).
- `history` : chronologie historique, archives, anciens présidents et bureaux.
- `awards` : galerie des récompenses et distinctions (filtres par année et niveau).
- `actions` : actions réalisées avec recherche, filtres dynamiques, page détaillée et galerie photo.
- `manifestations` : participations aux manifestations zonales et nationales, délégués et comptes rendus.

## Installation et lancement en local

1. Ouvrir un terminal dans le dossier `django_project` :
   ```bash
   cd django_project
   ```

2. Créer et activer un environnement virtuel Python :
   - **Windows (PowerShell)** :
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS** :
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurer les variables d'environnement (optionnel en local : si `TURSO_DATABASE_URL` est vide, Django utilise `db.sqlite3`) :
   ```bash
   cp .env.example .env
   ```
   Pour connecter le projet local directement à votre base **Turso**, renseignez dans `.env` :
   ```env
   TURSO_DATABASE_URL=libsql://votre-base-votre-compte.turso.io
   TURSO_AUTH_TOKEN=votre_jeton_turso
   ```

5. Appliquer les migrations :
   ```bash
   python manage.py makemigrations core history awards actions manifestations
   python manage.py migrate
   ```

6. Créer le compte administrateur unique :
   ```bash
   python manage.py createsuperuser
   ```

7. (Optionnel) Charger des fiches de démonstration clairement identifiées :
   ```bash
   python manage.py seed_demo
   ```

8. Lancer le serveur Django :
   ```bash
   python manage.py runserver
   ```

## Hébergement sur Render + Turso

1. Poussez le projet sur GitHub.
2. Sur **Render** (`dashboard.render.com`), créez un **Web Service** relié à votre dépôt :
   - **Root Directory** : `django_project` (si votre dépôt contient d'autres dossiers à la racine)
   - **Runtime** : `Python 3`
   - **Build Command** : `./build.sh`
   - **Start Command** : `gunicorn jci_project.wsgi:application --bind 0.0.0.0:$PORT`
3. Dans l'onglet **Environment** de Render, ajoutez :
   - `DJANGO_DEBUG` = `False`
   - `DJANGO_SECRET_KEY` = *(chaîne aléatoire longue et secrète)*
   - `TURSO_DATABASE_URL` = *(URL `libsql://...` ou `https://...` de votre base Turso)*
   - `TURSO_AUTH_TOKEN` = *(jeton d'authentification Turso)*
   - *(Optionnel pour créer l'admin au premier déploiement sur le plan gratuit)* : `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, `DJANGO_SUPERUSER_PASSWORD` (pensez à supprimer `DJANGO_SUPERUSER_PASSWORD` après le premier déploiement).

> **Note sur les fichiers médias (`media/`)** : Sur le plan gratuit de Render, le système de fichiers est éphémère à chaque redéploiement. Les images statiques du thème (`static/images/`, dont le logo officiel) sont conservées en permanence via WhiteNoise, mais les nouvelles photos téléversées depuis le dashboard nécessiteront ultérieurement un stockage externe (ex. Cloudinary / S3) ou un disque persistant Render.
