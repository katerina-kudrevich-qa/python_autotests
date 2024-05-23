import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'

TOKEN = '2a59404b5d24d39958723b20654bc753'

HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

TRAINER_ID = '4220'

def test_status_code():

    response = requests.get(url = f' {URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert    response.status_code == 200      

def test_part_of_response():
    response_get = requests.get(url = f' {URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_id"] == '4220'
