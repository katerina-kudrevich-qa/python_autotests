import requests

URL = 'https://api.pokemonbattle.me/v2'

TOKEN = '2a59404b5d24d39958723b20654bc753'

HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "Сэмми",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"

}

body_pokeball = {
      "pokemon_id": "28088"
}

body_name = {
     "pokemon_id": "28088",
    "name": "Nana",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response_create = requests.post(url =f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)



response_name = requests.put(url =f'{URL}/pokemons', headers = HEADER, json = body_name)
print (response_name.text)


response_pokeball = requests.post(url =f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print (response_pokeball.text)


