Structure de la Base de Données et des Modèles de Données
=========================================================

Cette section détaille la structure de la base de données pour l'application **Orange County Lettings**, y compris les modèles principaux et leurs champs, ainsi que les relations entre eux.

Modèles Principaux
------------------

**Profile:** 

Le modèle `Profile` représente le profil d'un utilisateur et possède une relation un-à-un avec le modèle `User` de Django. Il inclut des informations additionnelles sur l'utilisateur, telles que sa ville préférée.

- **Champs** :

  - `user` : Clé étrangère vers le modèle `User`, avec `on_delete=models.CASCADE` pour supprimer le profil si l'utilisateur est supprimé.
  
  - `favorite_city` : Ville préférée de l'utilisateur, champ `CharField` avec une longueur maximale de 64 caractères et optionnel.

- **Méthodes** :

  - `__str__` : Retourne le nom d'utilisateur associé au profil.
  
- **Options de Méta** :

  - `verbose_name` : Nom personnalisé pour le modèle dans l'interface d'administration.

  - `verbose_name_plural` : Nom pluriel pour le modèle dans l'interface d'administration.

Exemple de schéma du modèle `Profile` :

+----------------+----------------+----------------------------------------------+
| Attribut       | Type           | Description                                  |
+================+================+==============================================+
| user           | OneToOneField  | Référence au modèle User                     |
+----------------+----------------+----------------------------------------------+
| favorite_city  | CharField      | Ville préférée de l'utilisateur              |
+----------------+----------------+----------------------------------------------+

---

**Address:** 

Le modèle `Address` représente une adresse avec plusieurs champs, y compris le numéro de rue, le nom de la rue, la ville, l'état, le code postal et le code ISO du pays.

- **Champs** :

  - `number` : Numéro de rue, champ `PositiveIntegerField` avec un validateur de valeur maximale de 9999.

  - `street` : Nom de la rue, champ `CharField` avec une longueur maximale de 64 caractères.

  - `city` : Ville, champ `CharField` avec une longueur maximale de 64 caractères.

  - `state` : Code de l'état, champ `CharField` avec une longueur fixe de 2 caractères, validé avec un `MinLengthValidator`.

  - `zip_code` : Code postal, champ `PositiveIntegerField` avec une valeur maximale de 99999.

  - `country_iso_code` : Code ISO du pays, champ `CharField` avec une longueur fixe de 3 caractères, validé avec un `MinLengthValidator`.

- **Méthodes** :

  - `__str__` : Retourne une représentation de l'adresse sous forme de chaîne, avec le numéro et le nom de la rue.

- **Options de Méta** :

  - `verbose_name` et `verbose_name_plural` : Noms personnalisés pour le modèle dans l'interface d'administration.

Exemple de schéma du modèle `Address` :

+-------------------+----------------------+--------------------------------------+
| Attribut          | Type                 | Description                          |
+===================+======================+======================================+
| number            | PositiveIntegerField | Numéro de rue                        |
+-------------------+----------------------+--------------------------------------+
| street            | CharField            | Nom de la rue                        |
+-------------------+----------------------+--------------------------------------+
| city              | CharField            | Ville                                |
+-------------------+----------------------+--------------------------------------+
| state             | CharField            | Code de l'état (2 caractères)        |
+-------------------+----------------------+--------------------------------------+
| zip_code          | PositiveIntegerField | Code postal                          |
+-------------------+----------------------+--------------------------------------+
| country_iso_code  | CharField            | Code ISO du pays (3 caractères)      |
+-------------------+----------------------+--------------------------------------+

---

**Letting:**

Le modèle `Letting` représente une annonce de location et inclut un titre ainsi qu'une référence à une adresse.

- **Champs** :

  - `title` : Titre de la location, champ `CharField` avec une longueur maximale de 256 caractères.

  - `address` : Clé étrangère vers le modèle `Address`, avec `on_delete=models.CASCADE` pour supprimer l'annonce si l'adresse est supprimée.

- **Méthodes** :

  - `__str__` : Retourne le titre de la location.

Exemple de schéma du modèle `Letting` :

+----------+--------------+-----------------------------------+
| Attribut | Type         | Description                       |
+==========+==============+===================================+
| title    | CharField    | Titre de la location              |
+----------+--------------+-----------------------------------+
| address  | OneToOneField| Référence au modèle Address       |
+----------+--------------+-----------------------------------+

.. Important:: Ces modèles structurent la base de données de l'application et définissent les informations nécessaires pour gérer les profils des utilisateurs et les propriétés de location.
