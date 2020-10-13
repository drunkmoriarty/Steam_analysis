import pandas as pd 
import numpy as np
import requests
import json


def get_name_game(game_id):
    url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
    data=requests.get(url)
    data=data.json()
    return data  
