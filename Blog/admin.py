# blog/admin.py

from django.contrib import admin
from .models import Article

# Personnalisation de l'interface d'administration pour le modèle Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Colonnes à afficher dans la liste des articles
    list_display = ('titre', 'auteur', 'statut', 'date_creation')
    
    # Filtres dans la barre latérale de l'administration
    list_filter = ('statut', 'auteur')
    
    # Champs sur lesquels il est possible de rechercher
    search_fields = ('titre', 'contenu')
    
    # Pré-remplir le champ 'slug' avec le titre de l'article (si vous avez un champ slug dans le modèle)
    prepopulated_fields = {'slug': ('titre',)}
