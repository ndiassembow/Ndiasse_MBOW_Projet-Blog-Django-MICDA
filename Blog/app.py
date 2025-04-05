# blog/apps.py

from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = 'blog'  # Nom de l'application
    verbose_name = "Blog"  # Nom complet de l'application (peut être affiché dans l'admin)
