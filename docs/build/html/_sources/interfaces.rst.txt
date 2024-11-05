Interfaces de Programmation
===========================

Cette section décrit les interfaces de programmation de l'application **Orange County Lettings**.

Elle inclut les principales routes et vues disponibles pour interagir avec les profils et les annonces de location, ainsi que les messages d'erreur spécifiques.

Points d'Accès API
-------------------
Actuellement, l'application n'expose pas d'API REST ou d'API JSON pour des intégrations externes. Toutes les interactions avec l'application sont effectuées via des pages web rendues par Django.

Routes et Vues Principales
--------------------------

L'application **Orange County Lettings** est organisée en deux sections principales : **Profiles** et **Lettings**.

Chaque section a ses propres routes et vues, accessibles via les URL suivantes :

**Profiles:** 

Ces vues permettent de gérer les profils des utilisateurs.

- **`/profiles/`** : Affiche la liste de tous les profils disponibles.

  - **Vue** : `ProfileListView`

  - **Description** : Récupère tous les profils et les affiche dans une liste avec des liens vers chaque profil individuel.


- **`/profiles/<username>/`** : Affiche les détails d'un profil spécifique.

  - **Vue** : `ProfileDetailView`

  - **Description** : Affiche les informations détaillées pour un utilisateur spécifique, en utilisant le nom d'utilisateur pour récupérer le profil.


**Lettings:** 

Ces vues permettent de gérer les locations et les adresses associées.

- **`/lettings/`** : Affiche la liste de toutes les annonces de location.

  - **Vue** : `LettingListView`

  - **Description** : Récupère toutes les annonces de location et les affiche dans une liste avec des liens vers chaque annonce.


- **`/lettings/<id>/`** : Affiche les détails d'une annonce de location spécifique.

  - **Vue** : `LettingDetailView`

  - **Description** : Affiche les informations détaillées pour une annonce de location, identifiée par son identifiant unique.


Gestion des Erreurs
-------------------

L'application inclut des pages spécifiques pour gérer les erreurs standard.

- **404 - Page Not Found**

  - **Route** : N/A (automatique)

  - **Vue** : `404.html`

  - **Description** : Affiche un message d'erreur lorsque l'utilisateur essaie d'accéder à une page qui n'existe pas.


- **500 - Server Error**

  - **Route** : N/A (automatique)

  - **Vue** : `500.html`

  - **Description** : Affiche un message d'erreur lorsqu'une erreur serveur inattendue se produit.


.. Important:: Cette section des interfaces de programmation donne un aperçu des points d'accès et des vues principales, permettant de naviguer efficacement dans les différentes parties de l'application.