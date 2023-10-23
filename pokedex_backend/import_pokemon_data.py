# from models import Pokemon, Type, PokemonType, PokemonWeakness
import requests

# normal_type = Type.objects.create(name="Normal")
# fire_type = Type.objects.create(name="Fire")
# water_type = Type.objects.create(name="Water")
# grass_type = Type.objects.create(name="Grass")
# electric_type = Type.objects.create(name="Electric")
# ice_type = Type.objects.create(name="Ice")
# fighting_type = Type.objects.create(name="Figting")
# poison_type = Type.objects.create(name="Poison")
# ground_type = Type.objects.create(name="Ground")
# flying_type = Type.objects.create(name="Flying")
# psychic_type = Type.objects.create(name="Psychic")
# bug_type = Type.objects.create(name="Bug")
# rock_type = Type.objects.create(name="Rock")
# ghost_type = Type.objects.create(name="Ghost")
# dragon_type = Type.objects.create(name="Dragon")
# dark_type = Type.objects.create(name="Dark")
# steel_type = Type.objects.create(name="Steel")
# fairy_type = Type.objects.create(name="Fairy")

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

headers = {
    'content-type': 'application/json'
}
for i in range(1, 1018):
    url=f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url, headers=headers)
    data = response.json()
    pokemon = data["name"]
    pokemon_type = []
    for t in data["types"]:
        pokemon_type.append(t["type"]["name"])
    pokemon_weakness = []
    if len(pokemon_type) == 2:
        for j in range(len(type_matchup)):
            if type_matchup[j][type_name[pokemon_type[0]]] * type_matchup[j][type_name[pokemon_type[1]]] >= 2:
                pokemon_weakness.append(type_name_list[j])
    else:
        for j in range(len(type_matchup)):
            if type_matchup[j][type_name[pokemon_type[0]]] >= 2:
                pokemon_weakness.append(type_name_list[j])
    print(f"Pokemon: {pokemon} Type: {pokemon_type} Weakness: {pokemon_weakness}")
