import random
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pokemon, Album

@login_required
def buy_booster_pack(request):
    all_pokemons = list(Pokemon.objects.all())
    print("Todos los pokemones:", all_pokemons)

    random_pokemon = random.choice(all_pokemons)
    print("Pokemon aleatorio seleccionado:", random_pokemon)

    # Agregar el Pokémon aleatorio al álbum del usuario actual
    album, create = Album.objects.get_or_create(user=request.user)
    album.pokemons.add(random_pokemon)

    return render(request, 'album/buy_booster_pack.html', {'pokemon': random_pokemon})


def pokemon_details(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'album/pokemon_details.html', {'pokemon': pokemon})

@login_required
def view_album(request):
    # Obtener el álbum del usuario actual
    album = Album.objects.filter(user=request.user).first()

    # Verificar si el usuario tiene un álbum
    if album:
        # Obtener todos los Pokémon en el álbum del usuario
        pokemons = album.pokemons.all()
    else:
        pokemons = []

    return render(request, 'album/view_album.html', {'pokemons': pokemons})