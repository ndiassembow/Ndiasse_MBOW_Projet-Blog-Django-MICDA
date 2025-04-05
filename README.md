# Ndiasse_MBOW_Projet-Blog-Django-MICDA-2024-2025

Prénom & NOM :Ndiasse MBOW
INE : N0062AA20181
Niveau : Master 2 
Filière : MICDA
Matière : Langages et Frameworks Backend 2(php, java, python, js, c#)
Projet création d’un blog 
Tuteur : Abdourahmane BALDE

créons un dépôt (repository) sur GitHub
Ajoutons le code source complet du projet
Partageons le lien d'accès à ce dépôt :
abdourahmane.balde@unchk.edu.sn
master.micda@unchk.edu.sn




Outils à utiliser :
  vscode pycharm TablePlusSetup
  
Téléchargeons déjà python : 
  https://www.python.org/downloads/

Version python : 
  PS C:\Users\unchk\Desktop\ALL> py
  Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.

PIP : 
  >>> exit()
  PS C:\Users\unchk\Desktop\ALL> pip
  Usage:   
  pip <command> [options]
  Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.

Créer un environnement virtuel : 
  py -m venv myEnv

Activation environnement virtuel : 
  myEnv\Scripts\activate
  (myEnv) PS C:\Users\unchk\Desktop\ALL\_AV2_BG2Django_BG3C#_.Net> 

Installer la dernière version de django : 
  pip install django

Version de django : 
  django-admin –version
  (myEnv) PS C:\Users\unchk\Desktop\ALL\_AV2_BG2Django_BG3C#_.Net> django-admin --version
  5.2

Dépendance requirement : 
  pip freeze > requirements.tx

Créer un projet django blog ou notre choix de nom : 
  django-admin startproject lnoBlog

Lancement de lnoBlog : 
  py manage.py runserver 
  python manage.py migrate
  py manage.py runserver 
  The install worked successfully! Congratulations!
  View release notes for Django 5.2
  You are seeing this page because DEBUG=True is in your settings file and you have not configured any URLs.
  Django

Quittons vs code pour l’IDE PyCharm : 
  file > setting > project: _AV2_BG2Django_BG3C#_.Net > python interpreter
