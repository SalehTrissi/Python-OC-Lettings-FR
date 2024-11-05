Instructions sur l’Installation du Projet
=========================================

Cette section décrit les étapes pour installer **Orange County Lettings** en local et préparer l'environnement de développement.

Prérequis Techniques
--------------------
Avant de commencer, assurez-vous d’avoir installé les éléments suivants :

- **Python** 3.6 ou supérieur : pour exécuter l'application Django.
- **Git** : pour cloner le dépôt du projet.
- **SQLite3** : utilisé comme base de données locale.
- **Docker** (optionnel) : pour exécuter le projet dans un conteneur (utilisé pour le déploiement).

Étapes d'Installation
----------------------

1. **Cloner le Dépôt du Projet**

   Utilisez la commande suivante pour cloner le dépôt dans le répertoire de votre choix :

   ```
   git clone https://github.com/SalehTrissi/Python-OC-Lettings-FR.git
   ```

   ```
   cd Python-OC-Lettings-FR
   ```

2. **Créer un Environnement Virtuel**

   Créez un environnement virtuel pour isoler les dépendances du projet :

   ```
   python -m venv env
   ```

   Pour activer l’environnement virtuel :

   - Sur **Windows** :

    ```
    .\env\Scripts\Activate.ps1
    ```

   - Sur **macOS/Linux** :

    ```
    source env/bin/activate
    ```

3. **Installer les Dépendances**

   Une fois l’environnement virtuel activé, installez les dépendances nécessaires à partir du fichier `requirements.txt` :

   ```
   pip install -r requirements.txt
   ```

4. **Configurer la Base de Données**

   L'application utilise SQLite comme base de données par défaut. Appliquez les migrations pour configurer la base de données :

   ```
   python manage.py migrate
   ```

5. **Créer un Superutilisateur (Optionnel)**

   Si vous souhaitez accéder au panneau d’administration, créez un superutilisateur :

   ```
   python manage.py createsuperuser
   ```

6. **Lancer le Serveur de Développement**

   Démarrez le serveur Django pour vérifier que l'installation a réussi :

   ```
   python manage.py runserver
   ```

   Rendez-vous ensuite sur (http://localhost:8000) dans votre navigateur pour voir l'application en action.

.. Important:: Assurez-vous d'activer l'environnement virtuel (`env`) chaque fois que vous travaillez sur le projet.
