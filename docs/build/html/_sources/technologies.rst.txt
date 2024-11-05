Technologies et Langages de Programmation
=========================================

Le projet **Orange County Lettings** utilise plusieurs technologies et outils pour assurer un développement, un déploiement et une maintenance efficaces. Voici la liste des principales technologies utilisées, ainsi que leur rôle dans le projet.

Technologies Principales
------------------------

- **Python 3.8** : Langage de programmation principal, utilisé pour le développement de l'application et la gestion de la logique backend.

- **Django 3.x** : Framework web Python qui structure l'application, gère les interactions avec la base de données, et permet une gestion simple de l'interface et des données.

- **SQLite** : Base de données relationnelle légère utilisée pour le développement et le stockage local de données. En production, une autre base de données peut être utilisée selon les besoins.

- **Docker** : Technologie de conteneurisation utilisée pour isoler l’application dans un environnement standardisé, facilitant ainsi le déploiement et la gestion des dépendances.

- **Gunicorn** : Serveur WSGI utilisé pour exécuter l'application Django en production, permettant une gestion efficace des requêtes en environnement de production.

- **Whitenoise** : Outil de gestion des fichiers statiques, permettant à l'application de servir les fichiers CSS, JavaScript et images directement depuis le serveur sans avoir besoin d’un serveur HTTP externe.

Outils de Développement et Déploiement
--------------------------------------

- **Git** : Système de contrôle de version utilisé pour gérer le code source et suivre les modifications.

- **GitHub Actions** : Outil d'intégration continue (CI) et de déploiement continu (CD) utilisé pour automatiser les tests, le linting, la création d’images Docker, et le déploiement sur la plateforme d’hébergement.

- **Sentry** : Plateforme de surveillance et de suivi des erreurs. Permet de capturer, suivre, et résoudre les erreurs en temps réel, améliorant ainsi la fiabilité de l’application.

- **Render** : Plateforme d'hébergement pour le déploiement en production. Elle exécute l'application dans un conteneur Docker, en simplifiant la gestion de l'infrastructure et les mises à jour.

.. Important:: Ces technologies et outils sont intégrés pour garantir la stabilité, la performance et la maintenabilité de l'application, du développement jusqu'à la production.
