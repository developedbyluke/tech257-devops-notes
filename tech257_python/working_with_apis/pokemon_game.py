import random

import requests


def generate_random_id(number_of_pokemon):
    return random.randint(1, number_of_pokemon)


def attack_pokemon(attacker, defender):
    if defender['defence'] > 0:
        if defender['defence'] < attacker['attack']:
            damage = attacker['attack'] - defender['defence']
            defender['hp'] -= damage
            defender['defence'] = 0
        else:
            defender['defence'] -= attacker['attack']
    else:
        defender['hp'] -= attacker['attack']

    if defender['defence'] < 0:
        defender['defence'] = 0

    if defender['hp'] < 0:
        defender['hp'] = 0


# Get the number of Pokémon that exist from the API
# url = 'https://pokeapi.co/api/v2/pokemon/'
# response = requests.get(url)
# pokemon_count = json.loads(response.text)['count']
# DOESN'T WORK -> API returns a count of around 1300 but there are only 1025 Pokémon -> Hard code 1025 as Pokémon count

pokemon_count = 1025

pokemon_id_player = generate_random_id(pokemon_count)
pokemon_id_cpu = generate_random_id(pokemon_count)

pokemons = []

for index, pokemon_id in enumerate([pokemon_id_player, pokemon_id_cpu]):

    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemons.append({"name": pokemon_data['name']})

        for stat in pokemon_data['stats']:
            stat_name = stat['stat']['name']
            base_stat = stat['base_stat']

            if stat_name == 'attack':
                pokemons[index]['attack'] = base_stat
            elif stat_name == 'hp':
                pokemons[index]['hp'] = base_stat
            elif stat_name == 'defense':
                pokemons[index]['defence'] = base_stat
    else:
        print(f"There was an error getting pokemon: {response.text}")

pokemon_player = pokemons[0]
pokemon_cpu = pokemons[1]

print(f"Your pokemon is {pokemon_player['name']} with {pokemon_player['attack']} attack, {pokemon_player['defence']} defence, and {pokemon_player['hp']} health.")
print(f"Your opponent is {pokemon_cpu['name']} with {pokemon_cpu['attack']} attack, {pokemon_cpu['defence']} defence, and {pokemon_cpu['hp']} health.\n")

while pokemon_cpu['hp'] > 0 and pokemon_player['hp'] > 0:
    print(f"You attack dealing {pokemon_player['attack']} damage to the opponent.")
    attack_pokemon(pokemon_player, pokemon_cpu)
    if pokemon_cpu['hp'] == 0:
        break
    print(f"The opponent's HP is now {pokemon_cpu['hp']} and their defence is {pokemon_cpu['defence']}.")

    print(f"The opponent attacks dealing {pokemon_cpu['attack']} damage to you.")
    attack_pokemon(pokemon_cpu, pokemon_player)
    print(f"Your HP is now {pokemon_cpu['hp']} and your defence is {pokemon_cpu['defence']}.")

if pokemon_cpu['hp'] == 0:
    print("You win!")
else:
    print("You lose.")
