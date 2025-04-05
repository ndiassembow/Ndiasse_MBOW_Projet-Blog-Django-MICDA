# blog/views.py

from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article

# Liste des articles publiés
class ListeArticles(ListView):
    model = Article  # Le modèle utilisé pour afficher les articles
    template_name = 'blog/liste_articles.html'  # Le template à utiliser pour afficher la liste
    context_object_name = 'articles'  # Nom de la variable dans le template qui contient les articles

    # Personnalisation de la requête pour ne récupérer que les articles publiés
    def get_queryset(self):
        return Article.objects.filter(statut='publie')  # Seulement les articles publiés

# Création d'un nouvel article (nécessite que l'utilisateur soit connecté)
class CreerArticle(LoginRequiredMixin, CreateView):
    model = Article  # Le modèle pour la création d'un article
    fields = ['titre', 'contenu', 'image', 'statut']  # Les champs à afficher dans le formulaire
    template_name = 'blog/form_article.html'  # Template utilisé pour afficher le formulaire
    success_url = reverse_lazy('liste_articles')  # Redirection vers la liste des articles après succès

    # Attribution de l'auteur de l'article à l'utilisateur actuellement connecté
    def form_valid(self, form):
        form.instance.auteur = self.request.user  # L'auteur est l'utilisateur connecté
        return super().form_valid(form)
