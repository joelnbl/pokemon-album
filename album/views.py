import random
from django.shortcuts import render, get_object_or_404
from .models import Pokemon, Album

def buy_booster_pack(request):
    random_pokemons = random.sample(list(Pokemon.objects.all()), 5)
    context = {'pokemons': random_pokemons}
    return render(request, 'album/booster_pack.html', context)

def pokemon_details(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'album/pokemon_details.html', {'pokemon': pokemon})