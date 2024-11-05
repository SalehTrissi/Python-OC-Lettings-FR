Procédures de Déploiement et de Gestion de l’Application
========================================================

Cette section décrit le processus de déploiement de l'application **Orange County Lettings** en utilisant un pipeline CI/CD avec GitHub Actions et Render. Le déploiement automatique garantit que chaque modification validée dans le code source est testée, construite, et déployée en production sans intervention manuelle.


Déploiement Automatisé avec GitHub Actions
------------------------------------------

Le workflow de déploiement se divise en trois jobs principaux : `build`, `docker`, et `deploy`. Voici un aperçu de chaque étape :

**1. Job `build`:**

Le job `build` vérifie la qualité et la fiabilité du code avant de le préparer pour le déploiement. Il comprend les étapes suivantes :

- **Vérification du Code Source** :

  - Clone le code source depuis GitHub et installe les dépendances nécessaires.

  - Effectue le linting avec `flake8` pour vérifier la qualité du code.

  - Exécute les tests unitaires avec `pytest` et génère un rapport de couverture.


- **Génération de la Documentation** :

  - Utilise Sphinx pour générer la documentation technique du projet en HTML.

  - Les rapports de couverture de test et la documentation sont sauvegardés comme artifacts, permettant leur consultation ultérieure.


**2. Job `docker`:**

Une fois les tests réussis, le job `docker` construit et pousse une image Docker de l'application :

- **Configuration Docker** :

  - Configure Docker Buildx pour la construction multi-plateforme.

  - Se connecte à Docker Hub à l'aide des secrets GitHub `DOCKERHUB_USERNAME` et `DOCKERHUB_TOKEN`.


- **Création et Publication de l’Image Docker** :

  - Extrait les métadonnées (tags et labels) pour l’image Docker.

  - Construit et pousse l'image Docker sur Docker Hub, permettant une utilisation simplifiée dans l’environnement de production.


**3. Job `deploy`:**

Le job `deploy` déclenche le déploiement sur Render dès que l'image Docker est prête :


- **Déclenchement du Déploiement** :

  - Utilise l’URL du webhook de Render (`RENDER_DEPLOY_HOOK_URL`) pour déclencher automatiquement le déploiement de la nouvelle version.

  - Render récupère l'image Docker depuis Docker Hub et redéploie l’application en production.



Gestion Post-Déploiement
------------------------

Une fois l'application déployée, il est important d'assurer une gestion continue pour garantir la stabilité et la performance de l'application. Voici quelques bonnes pratiques pour la gestion post-déploiement :

- **Surveillance des Erreurs avec Sentry** :

  - Sentry est intégré pour suivre les erreurs et les exceptions en production.

  - Vérifiez régulièrement les rapports de Sentry pour identifier et résoudre les problèmes avant qu’ils n’affectent les utilisateurs.


- **Vérification des Logs** :

  - Consultez les logs de Render et de Docker pour surveiller les performances et identifier les problèmes potentiels.

  - Les logs peuvent aider à diagnostiquer des erreurs ou des problèmes de performance en production.


- **Mises à Jour du Code** :

  - Toute mise à jour du code dans les branches `main` ou `master` déclenche automatiquement le pipeline CI/CD, redéployant ainsi l'application après validation.

  - Avant chaque déploiement, assurez-vous que toutes les étapes CI/CD (tests, linting, etc.) se passent sans erreur.


Ce processus de déploiement automatisé garantit un flux de travail efficace, de la validation du code jusqu'au déploiement en production, réduisant les risques d'erreur humaine et assurant une livraison rapide des nouvelles fonctionnalités.
