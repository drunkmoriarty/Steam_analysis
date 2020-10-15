import pandas as pd 
import numpy as np
import requests
import json


def get_name_game(game_id):
    url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
    data=requests.get(url)
    data=data.json()
    return data  




def display_info(name_account, id_account, realname, account_country, nb_owned_games): 
    print('For the account named ', name_account, ':')
    print('The steam id is ', id_account)
    print('The name of the holder is ', realname)
    print('The account is stated in ', account_country)
    print('The owner of the account has ', nb_owned_games, ' games on steam')