Guide de Démarrage Rapide
=========================

Pour démarrer rapidement avec l'application **Orange County Lettings**, suivez les étapes ci-dessous. Ce guide propose deux méthodes : l'une utilisant Docker pour une configuration rapide et l'autre avec un environnement virtuel Python pour un démarrage en local.

Utilisation avec Docker
-----------------------

1. **Assurez-vous d’avoir Docker installé et en cours d’exécution**.
   
2. **Construisez l’image Docker et lancez un conteneur** :

   Depuis la racine du projet, exécutez les commandes suivantes :

   ```
   docker build -t oc-lettings-site .
   ```

   ```
   docker run -d -p 8000:8000 oc-lettings-site
   ```

3. **Accédez à l’application** :

   Une fois le conteneur démarré, ouvrez votre navigateur et rendez-vous sur (http://localhost:8000) pour voir l’application en action.


Démarrage en Local avec un Environnement Virtuel
-------------------------------------------------

1. **Cloner le Dépôt et Naviguer dans le Répertoire**

   ```
   git clone https://github.com/SalehTrissi/Python-OC-Lettings-FR.git
   ```

   ```
   cd Python-OC-Lettings-FR
   ```

2. **Créer et Activer un Environnement Virtuel**

   - Créez un environnement virtuel :

     ```
     python -m venv env
     ```

   - Activez l’environnement virtuel :

     - Sur **Windows** :
       ```
       .\env\Scripts\Activate.ps1
       ```

     - Sur **macOS/Linux** :
       ```
       source env/bin/activate
       ```

3. **Installer les Dépendances**

   ```
   pip install -r requirements.txt
   ```

4. **Appliquer les Migrations**

   Initialisez la base de données en appliquant les migrations :

   ```
   python manage.py migrate
   ```

5. **Lancer le Serveur de Développement**

   Démarrez le serveur Django :

   ```
   python manage.py runserver
   ```

   Ouvrez (http://localhost:8000) dans votre navigateur pour vérifier le bon fonctionnement de l'application.

.. Important:: Assurez-vous d’activer l’environnement virtuel chaque fois que vous travaillez sur le projet en local.
