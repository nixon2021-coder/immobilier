
from unicodedata import name
from django.db import models

class Banner(models.Model):
    image = models.FileField()
    titre = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)


class About(models.Model):
     description = models.CharField(max_length = 200)
     titre = models.CharField(max_length = 200)
     image = models.FileField()
     libelle = models.CharField(max_length=100)
     create_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)
     statut = models.BooleanField(default=True)

class Service(models.Model):
    image = models.FileField()
    titre = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class Gallery(models.Model):
    description = models.CharField(max_length = 200)
    image = models.FileField()
    titre = models.CharField(max_length = 200)
    adresse = models.CharField(max_length = 200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class Properties(models.Model):
    description = models.CharField(max_length = 200)
    image = models.FileField()
    titre = models.CharField(max_length = 200)
    libelle = models.CharField(max_length = 200)
    nom = models.CharField(max_length=50)
    date = models.DateTimeField(max_length=100)
    Icon = models.CharField(max_length=100)
    prix= models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)

class Reseausocial(models.Model):
    nom = models.CharField(max_length=50)
    Icon = models.CharField(max_length=100)
    lien = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)



class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    prix = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    Message =  models.EmailField(max_length=2254)
    email = models.EmailField(max_length=254)
    numero = models.IntegerField(default=1, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)


class Customers(models.Model):
    titre = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    nom = models.CharField(max_length=50)
    image = models.FileField()
    libelle = models.CharField(max_length = 200)


class Slide(models.Model):
    image = models.FileField()
    titre = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
   

    





