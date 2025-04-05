# blog/models.py

from django.db import models
from django.contrib.auth.models import User

# Définition du modèle Article
class Article(models.Model):
    # Définition des choix pour le statut de l'article (brouillon ou publié)
    STATUT_CHOIX = [
        ('brouillon', 'Brouillon'),
        ('publie', 'Publié'),
    ]

    # Champs du modèle
    titre = models.CharField(max_length=200)  # Le titre de l'article
    contenu = models.TextField()  # Le contenu de l'article
    date_creation = models.DateTimeField(auto_now_add=True)  # Date de création de l'article
    date_maj = models.DateTimeField(auto_now=True)  # Date de dernière mise à jour de l'article
    statut = models.CharField(max_length=10, choices=STATUT_CHOIX, default='brouillon')  # Statut de l'article
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)  # L'auteur de l'article, lié à un utilisateur
    image = models.ImageField(upload_to='articles/', blank=True)  # Image associée à l'article

    # Méthode pour afficher le titre de l'article dans l'interface d'administration
    def __str__(self):
        return self.titre
