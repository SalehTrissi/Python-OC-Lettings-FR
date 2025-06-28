############################
Installation Locale
############################

Ce guide vous explique comment installer et lancer le projet sur votre machine locale pour le développement.

Prérequis
=========
* Python 3.11 ou supérieur
* Git

Étapes d'installation
=====================

1. **Clonez le dépôt**
   Ouvrez un terminal et clonez le dépôt depuis GitHub :
   .. code-block:: bash

      git clone https://github.com/SalehTrissi/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. **Créez un environnement virtuel**
   Il est fortement recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.
   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Sur Windows: venv\Scripts\activate

3. **Installez les dépendances**
   Installez tous les paquets nécessaires listés dans le fichier `requirements.txt`.
   .. code-block:: bash

      pip install -r requirements.txt

4. **Appliquez les migrations**
   Cette commande met en place la base de données en utilisant le fichier `oc-lettings-site.sqlite3` fourni.
   .. code-block:: bash

      python manage.py migrate

5. **Lancez le serveur de développement**
   Votre projet est maintenant prêt ! Lancez le serveur local.
   .. code-block:: bash

      python manage.py runserver

   Vous pouvez maintenant accéder au site à l'adresse http://127.0.0.1:8000.


Accès à l'Interface d'Administration
=====================================

L'interface d'administration est disponible à l'adresse http://127.0.0.1:8000/admin.

Pour la base de données fournie avec le projet, vous pouvez utiliser les identifiants suivants :

* **Nom d'utilisateur** : `admin`
* **Mot de passe** : `Abc1234!`

.. warning::
   Ces identifiants sont destinés **uniquement au développement local**. Ne les utilisez jamais dans un environnement de production.

Si vous démarrez avec une base de données vide, vous devrez créer votre propre superutilisateur avec la commande suivante :

.. code-block:: bash

   python manage.py createsuperuser