from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    details = models.TextField()

class Album(models.Model):
    name = models.CharField(max_length=100)
    pokemons = models.ManyToManyField(Pokemon)