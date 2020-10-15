import pandas as pd 
import numpy as np
import requests
import json

def open_data():
    with open('data_profil.json', 'r') as jsonfile:
        data=json.load(jsonfile)
    return data

def get_name_game(game_id):
    url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
    database_games=requests.get(url)
    database_games=database_games.json()
    return database_games

def display_info(name_account, id_account, realname, account_country, nb_owned_games): 
    print('For the account named ', name_account, ':')
    print('The steam id is ', id_account)
    print('The name of the holder is ', realname)
    print('The account is stated in ', account_country)
    print('The owner of the account has ', nb_owned_games, ' games on steam')