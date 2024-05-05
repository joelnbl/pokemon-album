from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    details = models.TextField()
    def __str__(self):
        return self.name

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pokemons = models.ManyToManyField('Pokemon')

    def __str__(self):
        return f"Album de {self.user.username}"