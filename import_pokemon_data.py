import os
import django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pokedex_backend.settings")
django.setup()

from pokedex_backend.models import Pokemon, Type, PokemonType, PokemonWeakness

normal_type, normal_created = Type.objects.get_or_create(name="Normal")
fire_type, fire_created = Type.objects.get_or_create(name="Fire")
water_type, water_created = Type.objects.get_or_create(name="Water")
grass_type, grass_created = Type.objects.get_or_create(name="Grass")
electric_type, electric_created = Type.objects.get_or_create(name="Electric")
ice_type, ice_created = Type.objects.get_or_create(name="Ice")
fighting_type, fighting_created = Type.objects.get_or_create(name="Figting")
poison_type, poison_created = Type.objects.get_or_create(name="Poison")
ground_type, ground_created = Type.objects.get_or_create(name="Ground")
flying_type, flying_created = Type.objects.get_or_create(name="Flying")
psychic_type, psychic_created = Type.objects.get_or_create(name="Psychic")
bug_type, bug_created = Type.objects.get_or_create(name="Bug")
rock_type, rock_created = Type.objects.get_or_create(name="Rock")
ghost_type, ghost_created = Type.objects.get_or_create(name="Ghost")
dragon_type, dragon_created = Type.objects.get_or_create(name="Dragon")
dark_type, dark_created = Type.objects.get_or_create(name="Dark")
steel_type, steel_created = Type.objects.get_or_create(name="Steel")
fairy_type, fairy_created = Type.objects.get_or_create(name="Fairy")

type_name = {
    "normal": 0,
    "fire": 1,
    "water": 2,
    "grass": 3,
    "electric": 4,
    "ice": 5,
    "fighting": 6,
    "poison": 7,
    "ground": 8,
    "flying": 9,
    "psychic": 10,
    "bug": 11,
    "rock": 12,
    "ghost": 13,
    "dragon": 14,
    "dark": 15,
    "steel": 16,
    "fairy": 17,
}

type_name_model = {
    "normal": normal_type,
    "fire": fire_type,
    "water": water_type,
    "grass": grass_type,
    "electric": electric_type,
    "ice": ice_type,
    "fighting": fighting_type,
    "poison": poison_type,
    "ground": ground_type,
    "flying": flying_type,
    "psychic": psychic_type,
    "bug": bug_type,
    "rock": rock_type,
    "ghost": ghost_type,
    "dragon": dragon_type,
    "dark": dark_type,
    "steel": steel_type,
    "fairy": fairy_type,
}

type_name_list = [
    "normal",
    "fire",
    "water",
    "grass",
    "electric",
    "ice",
    "fighting",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dragon",
    "dark",
    "steel",
    "fairy",
]

# fmt: off
type_matchup = [
#      N    F    W    G    E    I    F    P    G    F    P    B    R    G    D    D    S    F
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   0,   1,   1, 0.5,   1], # Normal
    [  1, 0.5, 0.5,   2,   1,   2,   1,   1,   1,   1,   1,   2, 0.5,   1, 0.5,   1,   2,   1], # Fire
    [  1,   2, 0.5, 0.5,   1,   1,   1,   1,   2,   1,   1,   1,   2,   1, 0.5,   1,   1,   1], # Water
    [  1, 0.5,   2, 0.5,   1,   1,   1, 0.5,   2, 0.5,   1, 0.5,   2,   1, 0.5,   1, 0.5,   1], # Grass
    [  1,   1,   2, 0.5, 0.5,   1,   1,   1,   0,   2,   1,   1,   1,   1, 0.5,   1,   1,   1], # Electric
    [  1, 0.5, 0.5,   2,   1, 0.5,   1,   1,   2,   2,   1,   1,   1,   1,   2,   1, 0.5,   1], # Ice
    [  2,   1,   1,   1,   1,   2,   1, 0.5,   1, 0.5, 0.5, 0.5,   2,   0,   1,   2,   2, 0.5], # Fighting
    [  1,   1,   1,   2,   1,   1,   1, 0.5, 0.5,   1,   1,   1, 0.5, 0.5,   1,   1,   0,   2], # Poison
    [  1,   2,   1, 0.5,   2,   1,   1,   2,   1,   0,   1, 0.5,   2,   1,   1,   1,   2,   1],# Ground
    [  1,   1,   1,   2, 0.5,   1,   2,   1,   1,   1,   1,   2, 0.5,   1,   1,   1, 0.5,   1], # Flying
    [  1,   1,   1,   1,   1,   1,   2,   2,   1,   1, 0.5,   1,   1,   1,   1,   0, 0.5,   1], # Psychic
    [  1, 0.5,   1,   2,   1,   1, 0.5, 0.5,   1, 0.5,   2,   1,   1, 0.5,   1,   2, 0.5, 0.5], # Bug
    [  1,   2,   1,   1,   1,   2, 0.5,   1, 0.5,   2,   1,   2,   1,   1,   1,   1, 0.5,   1], # Rock
    [  0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1,   1], # Ghost
    [  1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1, 0.5,   0], # Dragon
    [  1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1, 0.5], # Dark
    [  1, 0.5, 0.5,   1, 0.5,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1, 0.5,   2], # Steel
    [  1, 0.5,   1,   1,   1,   1,   2, 0.5,   1,   1,   1,   1,   1,   0,   2,   2, 0.5,   1] # Fairy
]
# fmt: on
headers = {"content-type": "application/json"}
for i in range(1, 1018):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url, headers=headers)
    data = response.json()
    pokemon: str = data["name"]
    pokemon = pokemon.capitalize()
    pokemon_type = []
    for t in data["types"]:
        pokemon_type.append(t["type"]["name"])
    pokemon_weakness = []
    if len(pokemon_type) == 2:
        for j in range(len(type_matchup)):
            if (
                type_matchup[j][type_name[pokemon_type[0]]]
                * type_matchup[j][type_name[pokemon_type[1]]]
                >= 2
            ):
                pokemon_weakness.append(type_name_list[j])
    else:
        for j in range(len(type_matchup)):
            if type_matchup[j][type_name[pokemon_type[0]]] >= 2:
                pokemon_weakness.append(type_name_list[j])
    pokemon_model, pokemon_model_created = Pokemon.objects.get_or_create(
        name=pokemon, pokedex_number=i
    )
    if pokemon_model_created:
        for t in pokemon_type:
            PokemonType.objects.create(pokemon=pokemon_model, type=type_name_model[t])
        for w in pokemon_weakness:
            PokemonWeakness.objects.create(
                pokemon=pokemon_model, type=type_name_model[w]
            )
    # print(f"Pokemon: {pokemon} Type: {pokemon_type} Weakness: {pokemon_weakness}")
