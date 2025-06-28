# Résumé

## Orange County Lettings

Site web d'Orange County Lettings

[![Documentation Status](https://readthedocs.org/projects/trissi-mohammad-saleh-python-oc-lettings-fr/badge/?version=latest)](https://trissi-mohammad-saleh-python-oc-lettings-fr.readthedocs.io/fr/latest/?badge=latest)

This is a Django project for managing real estate lettings, refactored from a monolithic architecture to a modular one.

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

## Déploiement

Ce projet est configuré pour l'Intégration Continue (CI) et le Déploiement Continu (CD) en utilisant GitHub Actions, Docker et Render.

### Résumé du fonctionnement

Le pipeline de déploiement est automatisé et suit les étapes suivantes :

1. **Déclencheur** : Un `push` vers la branche `master` déclenche automatiquement le workflow GitHub Actions.
2. **Compilation & Tests (CI)** : Le workflow exécute d'abord un job "Build and Test" qui installe les dépendances, lance le linter (`flake8`), et exécute la suite de tests complète (`pytest`). Il vérifie également que la couverture de test est supérieure à 80 %. Ce job doit réussir pour que le pipeline puisse continuer.
3. **Containerize  (CI)** : Si les tests réussissent, un job "Containerize" construit une image Docker de l'application. Cette image est ensuite taguée avec le SHA unique du commit Git et poussée sur Docker Hub.
4. **Déploiement (CD)** : Si l'image est poussée avec succès, un dernier job "Deploy" est déclenché. Ce job appelle un "Deploy Hook" spécifique fourni par Render, qui ordonne à Render de récupérer la dernière version de la branche `master` et de redéployer le service avec le nouveau code.

Les modifications poussées sur toute autre branche ne déclencheront que le job "Build & Test", garantissant la qualité du code sans le déployer en production.

### Configuration Requise

Pour exécuter ce pipeline de déploiement sur votre propre version du projet (fork), vous devrez configurer les éléments suivants :

#### 1. Secrets du dépôt sur GitHub

Naviguez vers les `Settings` > `Secrets and variables` > `Actions` de votre dépôt GitHub et ajoutez les secrets suivants :

- `DOCKERHUB_USERNAME` : Votre nom d'utilisateur Docker Hub.
- `DOCKERHUB_TOKEN` : Un token d'accès généré depuis votre compte Docker Hub avec les permissions `Read, Write, Delete`.
- `RENDER_DEPLOY_HOOK_URL` : L'URL du "Deploy Hook" fournie par votre service web sur Render (disponible dans l'onglet `Settings` du service).

#### 2. Variables d'environnement sur Render

Sur le tableau de bord Render, pour votre service web, naviguez vers l'onglet `Environment` et ajoutez les variables suivantes :

- `DJANGO_SECRET_KEY` : Une nouvelle clé secrète générée aléatoirement pour l'environnement de production.
- `SENTRY_DSN` : La clé DSN de votre projet Sentry.
- `DEBUG` : À définir sur `False`.
- `ALLOWED_HOSTS` : L'URL de votre application Render (par exemple, `votre-nom-d-app.onrender.com`).

### Étapes du Déploiement

Une fois la configuration initiale terminée, le processus de déploiement est entièrement automatisé.

1. **Commit et Push** : Faites vos modifications dans le code de l'application.
2. **Fusionner sur Master** : Assurez-vous que vos modifications sont sur la branche `master`.
3. **Pousser sur GitHub** :

    ```bash
    git push origin master
    ```

4. **Suivre le Pipeline** : Vous pouvez observer la progression du déploiement dans l'onglet "Actions" de votre dépôt GitHub. Une fois que tous les jobs sont réussis, Render démarrera automatiquement le nouveau déploiement, qui peut être suivi depuis l'onglet "Events" de votre tableau de bord Render.
