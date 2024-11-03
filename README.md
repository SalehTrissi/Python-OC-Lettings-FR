## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---

## 🚀 Déploiement

### 1. Récapitulatif du Déploiement

Le déploiement de ce projet est automatisé grâce à **GitHub Actions** et à un webhook de déploiement fourni par **Render**. Lorsque les tests et l’analyse de code sont réussis, le pipeline CI/CD :
1. Construit une image Docker,
2. La pousse vers **Docker Hub**,
3. Déclenche un déploiement sur Render.

Ainsi, chaque mise à jour sur les branches `main` ou `master` est déployée après une validation complète du code.

### 2. Configuration Requise

Pour que le déploiement fonctionne correctement, assurez-vous de disposer des éléments suivants :

- **Secrets GitHub** configurés :
  - `DOCKERHUB_USERNAME` et `DOCKERHUB_TOKEN` : pour l’authentification Docker Hub.
  - `RENDER_DEPLOY_HOOK_URL` : pour déclencher le déploiement via Render.

- **Compte Docker Hub** : avec un dépôt configuré pour héberger l’image Docker.
- **Compte Render** : avec un service configuré pour exécuter l’application à partir d’un conteneur Docker.

### 3. Étapes de Déploiement

#### Préparation

1. **Créer et configurer les secrets GitHub** :
   - Accédez aux **Paramètres** du dépôt GitHub, puis à **Secrets et variables > Actions**.
   - Ajoutez les secrets suivants :
     - **DOCKERHUB_USERNAME** : votre nom d’utilisateur Docker Hub.
     - **DOCKERHUB_TOKEN** : un token d’accès généré dans Docker Hub (via `Compte > Paramètres > Sécurité`).
     - **RENDER_DEPLOY_HOOK_URL** : l’URL du hook de déploiement Render (disponible dans les paramètres du service Render sous *Deploy Hook*).

2. **Configurer Docker Hub** :
   - Créez un dépôt (public ou privé) sur Docker Hub nommé `oc-lettings-site`.
   - Ce dépôt recevra les images Docker automatiquement poussées par le workflow GitHub Actions.

3. **Configurer Render** :
   - Créez un service Render basé sur une image Docker.
   - Configurez le service pour utiliser l’image de Docker Hub : `DOCKERHUB_USERNAME/oc-lettings-site`.
   - Copiez l’URL du *Deploy Hook* depuis les paramètres du service Render pour l’ajouter comme secret dans GitHub.

#### Déploiement Automatique

1. **Déclenchement** :
   - Le déploiement est automatiquement déclenché pour les *pushes* sur les branches `main` ou `master`.
   - Les étapes du workflow incluent la construction de l’image, le linting, les tests, la vérification de la couverture de test, le push de l'image vers Docker Hub, puis le déclenchement du déploiement via le webhook Render.

2. **Vérification du Déploiement** :
   - Render lance automatiquement le déploiement à la suite du webhook.
   - Une fois le déploiement terminé, le service est accessible à l’URL configurée sur Render.

### ⚙️ Instructions Additionnelles

- Pour des modifications sur les branches de déploiement (`main` ou `master`), assurez-vous que toutes les étapes CI/CD se valident avant le déploiement.
- En cas de modification d’un secret (ex. : renouvellement de token), mettez à jour le secret correspondant dans GitHub pour garantir un déploiement continu et sans interruption.

---