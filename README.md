# Orange County Lettings

Ce document décrit les étapes pour le développement local et le déploiement de l'application **Orange County Lettings**.

---

## ⚙️ Développement Local

### Prérequis

Pour configurer l'environnement de développement, assurez-vous de disposer des éléments suivants :

- Compte GitHub avec accès en lecture au dépôt de ce projet.
- **Git CLI** pour gérer le code source.
- **SQLite3 CLI** pour interagir avec la base de données.
- **Python 3.6 ou supérieur**.

**Note** : Il est supposé que la commande `python` de votre shell exécute l'interpréteur Python approprié. Sinon, activez un environnement virtuel pour garantir l'usage de la version correcte.

### Installation et Configuration

#### macOS / Linux

1. **Cloner le dépôt :**
   ```bash
   cd /path/to/your/project
   git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
   ```
   OR
    ```bash
   git clone https://github.com/SalehTrissi/Python-OC-Lettings-FR.git
   ```

2. **Créer un environnement virtuel :**
   ```bash
   cd Python-OC-Lettings-FR
   python -m venv venv
   ```
   Si vous rencontrez des erreurs sous Ubuntu, installez le package :
   ```bash
   sudo apt-get install python3-venv
   ```

3. **Activer l'environnement virtuel :**
   ```bash
   source venv/bin/activate
   ```

4. **Vérifier l'environnement :**
   - Confirmez que `python` pointe vers la version de l'environnement virtuel :
     ```bash
     which python
     ```
   - Confirmez la version Python (3.6 ou supérieure) :
     ```bash
     python --version
     ```
   - Confirmez que `pip` est dans l'environnement virtuel :
     ```bash
     which pip
     ```

5. **Désactiver l'environnement virtuel :**
   ```bash
   deactivate
   ```

#### Exécuter le Site

1. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

2. **Lancer le serveur :**
   ```bash
   python manage.py runserver
   ```
   Accédez à l'URL [http://localhost:8000](http://localhost:8000) pour vérifier le bon fonctionnement du site.

#### Linting et Tests

- **Exécuter l'analyse statique avec Flake8 :**
  ```bash
  flake8
  ```
- **Lancer les tests unitaires :**
  ```bash
  pytest
  ```

#### Gestion de la Base de Données

1. **Ouvrir une session SQLite :**
   ```bash
   sqlite3
   ```
2. **Se connecter à la base de données :**
   ```sqlite
   .open oc-lettings-site.sqlite3
   ```
3. **Afficher les tables :**
   ```sqlite
   .tables
   ```
4. **Examiner la table des profils :**
   ```sqlite
   pragma table_info(Python-OC-Lettings-FR_profile);
   ```
5. **Lancer une requête d'exemple :**
   ```sqlite
   select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
   ```
6. **Quitter SQLite :**
   ```sqlite
   .quit
   ```

#### Accéder au Panel d'Administration

- Connectez-vous sur [http://localhost:8000/admin](http://localhost:8000/admin) avec les identifiants :
  - **Utilisateur** : `admin`
  - **Mot de passe** : `Abc1234!`

### Guide pour Windows

Utilisez **PowerShell** avec les adaptations suivantes :

- Activation de l'environnement virtuel :
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- Remplacez `which <commande>` par :
  ```powershell
  (Get-Command <commande>).Path
  ```

---

## 🚀 Déploiement

### Aperçu du Déploiement

Ce projet utilise un pipeline **CI/CD** géré par **GitHub Actions** et **Render** pour un déploiement automatisé. Une fois les tests et l’analyse de code validés, le processus de déploiement suit les étapes ci-dessous :

1. Construction de l’image Docker.
2. Publication de l’image sur **Docker Hub**.
3. Déclenchement du déploiement via le webhook de **Render**.

Ainsi, chaque modification poussée sur les branches `main` ou `master` déclenche un déploiement après validation.

### Configuration Requise

Assurez-vous d’avoir les éléments suivants pour garantir le bon fonctionnement du déploiement :

- Secrets GitHub configurés :
  - **DOCKERHUB_USERNAME** et **DOCKERHUB_TOKEN** : pour l'authentification sur Docker Hub.
  - **RENDER_DEPLOY_HOOK_URL** : pour déclencher le déploiement sur Render.
- Compte **Docker Hub** avec un dépôt configuré (`oc-lettings-site`).
- Compte **Render** avec un service configuré pour exécuter l’application.

### Étapes de Déploiement

#### Préparation des Secrets GitHub

1. **Créer les secrets** :
   - Allez dans **Paramètres > Secrets et variables > Actions** du dépôt GitHub.
   - Ajoutez les secrets suivants :
     - **DOCKERHUB_USERNAME** : votre nom d’utilisateur Docker Hub.
     - **DOCKERHUB_TOKEN** : un token d’accès Docker Hub.
     - **RENDER_DEPLOY_HOOK_URL** : l’URL du webhook Render.

#### Configurer Docker Hub

1. Créez un dépôt `oc-lettings-site` (public ou privé) pour héberger les images Docker.
2. Ce dépôt recevra automatiquement les images poussées par GitHub Actions.

#### Configurer Render

1. Créez un service Render pour exécuter l’application à partir d’une image Docker.
2. Configurez le service pour utiliser l’image Docker Hub : `DOCKERHUB_USERNAME/oc-lettings-site`.
3. Récupérez l’URL du **Deploy Hook** pour l’ajouter aux secrets GitHub.

### Déploiement Automatique

1. **Déclenchement** :
   - Les *pushes* sur les branches `main` ou `master` déclenchent automatiquement le déploiement.
   - Le pipeline effectue le linting, les tests, la vérification de la couverture, la publication sur Docker Hub, puis le déploiement via Render.

2. **Vérification** :
   - Une fois le déploiement terminé, accédez au service via l’URL configurée dans Render.

---

## 📝 Remarques

- Toute modification des branches `main` ou `master` est automatiquement déployée.
- Si un secret est modifié (par exemple, le token Docker), mettez-le à jour dans GitHub pour éviter toute interruption du déploiement.

--- 