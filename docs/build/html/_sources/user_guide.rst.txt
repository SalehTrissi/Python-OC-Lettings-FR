Guide d’Utilisation
====================

Ce guide fournit des instructions sur l'utilisation de l'application **Orange County Lettings** et décrit les fonctionnalités principales, ainsi que des exemples de cas d'utilisation pour différents types d'utilisateurs.


Fonctionnalités Principales
---------------------------

L'application est divisée en deux sections principales : **Profiles** et **Lettings**. Chaque section offre des fonctionnalités spécifiques pour les utilisateurs.

**Profiles :**

La section "Profiles" permet aux utilisateurs de voir la liste de tous les profils et d'accéder aux détails de chaque utilisateur.

- **Accéder à la liste des profils** :

  - Naviguez vers `/profiles/` pour voir la liste de tous les profils enregistrés.

  - Chaque profil est affiché sous forme de lien, permettant un accès rapide aux informations de chaque utilisateur.

- **Voir les détails d'un profil** :

  - En cliquant sur un nom d'utilisateur dans la liste des profils, vous accédez à la page de détails de ce profil.

  - La page de détails montre les informations de base de l'utilisateur, comme son prénom, nom, email, et ville préférée.


**Cas d'utilisation : Visualiser les profils d’utilisateurs**

- **But** : Un administrateur ou un utilisateur souhaite vérifier les informations de profil d'un autre utilisateur.


- **Étapes** :

  1. L’utilisateur navigue vers `/profiles/`.

  2. Il clique sur le nom d'utilisateur souhaité pour accéder aux détails.

  3. Les informations du profil sont affichées, permettant à l'utilisateur de consulter les détails du profil sélectionné.


**Lettings :**

La section "Lettings" permet aux utilisateurs de consulter la liste des annonces de location et d'accéder aux détails de chaque annonce.

- **Accéder à la liste des locations** :

  - Allez sur `/lettings/` pour voir une liste de toutes les annonces de location disponibles.

  - Chaque annonce est affichée avec un lien vers ses détails, facilitant la navigation.


- **Voir les détails d'une location** :

  - En cliquant sur le titre d'une annonce dans la liste, vous accédez aux informations détaillées de cette annonce.

  - La page de détails comprend l'adresse complète, avec le numéro, la rue, la ville, l'état, le code postal et le code ISO du pays.


**Cas d'utilisation : Consulter une annonce de location**

- **But** : Un utilisateur souhaite voir les détails d'une annonce de location spécifique pour évaluer si elle correspond à ses besoins.

- **Étapes** :

  1. L’utilisateur se rend sur `/lettings/`.

  2. Il clique sur l'annonce souhaitée pour voir les détails.

  3. La page de l'annonce s'ouvre, affichant toutes les informations de localisation pertinentes.


Gestion des Erreurs
-------------------

L'application fournit des pages d'erreur claires pour aider les utilisateurs en cas de problème.

- **Page 404 - Page Not Found** : S'affiche lorsque l'utilisateur tente d'accéder à une URL non valide. Un lien de retour à l'accueil est proposé.

- **Page 500 - Server Error** : S'affiche lorsqu'un problème serveur se produit. Elle informe l'utilisateur de l'erreur et propose un retour à l'accueil.



**Cas d'utilisation : Gestion des erreurs**

- **But** : Un utilisateur tente d'accéder à une page qui n'existe pas.

- **Étapes** :

  1. L'utilisateur entre une URL non valide.

  2. La page 404 apparaît, indiquant que la page n'existe pas.

  3. L'utilisateur clique sur le lien pour retourner à la page d'accueil.



Conclusion
----------

L'application **Orange County Lettings** est conçue pour être intuitive et facile à naviguer. En suivant les étapes ci-dessus, les utilisateurs peuvent facilement accéder aux informations de profil et de location, tout en bénéficiant d'une interface conviviale pour gérer les erreurs éventuelles.
