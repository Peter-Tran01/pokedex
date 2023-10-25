from django.http import JsonResponse
from pokedex_backend.models import Pokemon, Type, PokemonType, PokemonWeakness


def search_pokemon(request):
    search_query = request.GET.get("query", "")

    pokemon_query = Pokemon.objects.filter(name__icontains=search_query)
    return_data = []
    for pokemon in pokemon_query:
        pokemon_type = pokemon.pokemontype_set.all()
        pokemon_weakness = pokemon.pokemonweakness_set.all()
        pokemon_data = {
            "pokedex_number": pokemon.pokedex_number,
            "pokemon": pokemon.name,
            "type": [type.type.name for type in pokemon_type],
            "weakness": [weakness.type.name for weakness in pokemon_weakness],
        }
        return_data.append(pokemon_data)

    return JsonResponse(return_data, safe=False)
