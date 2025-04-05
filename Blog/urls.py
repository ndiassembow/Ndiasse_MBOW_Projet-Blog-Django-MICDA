# blog/urls.py

from django.urls import path
from .views import ListeArticles, CreerArticle

# Définition des URLs pour l'application Blog
urlpatterns = [
    # URL pour la liste des articles publiés
    path('', ListeArticles.as_view(), name='liste_articles'),
    
    # URL pour la création d'un nouvel article (accessible aux utilisateurs connectés)
    path('nouvel-article/', CreerArticle.as_view(), name='creer_article'),
]
