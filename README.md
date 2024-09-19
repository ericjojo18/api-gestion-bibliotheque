#  API-GESTION-BIBLIOTHEQUE

## Description
    Ce projet est un système de gestion de bibliothèque en ligne utilisant Django et une API RESTful pour gérer les livres, les emprunts et les utilisateurs. Les fonctionnalités incluent la recherche de livres, la réservation de livres et la gestion des retours.

## Technologies Utilisées
    Exigences Techniques
    Python : 3.12.x ou supérieur
    Django : 5.x ou supérieur
    Base de données : PostgreSQL
    API REST : Implémentée avec Django REST Framework
    Documentation API : Documentée avec Postman



### Prérequis
    Python 3.12.x ou supérieur
    PostgreSQL
    Git (pour cloner le projet)

## Installation

### Étapes

1. **Cloner le Repository**
    git clone https://github.com/ericjojo18/api-gestion-bibliotheque.git
    cd gestion-bibliotheque

2. Créer un environnement virtuel

    python -m venv venv
    source venv/bin/activate (Pour Linux/Mac)
    venv\Scripts\activate    (Pour Windows)

3. Installer les dépendances

     install -r requirements.txt

4. Créer et Configurer la base de données PostgreSQL appelée library_db


    -Pour la création lancez votre pg admin et faites la création de la base de donnée
    -Pour la configuration dans settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'postgres',
        'PASSWORD': 'le mot de passe de votre postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Faire et Appliquer les migrations
    -python manage.py makemigrations
    -python manage.py migrate

7. Lancer le serveur de développement

    -python manage.py runserver




