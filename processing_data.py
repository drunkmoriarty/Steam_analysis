import pandas as pd 
import numpy as np
import requests
import json

def open_data():
    with open('data_profil.json', 'r') as jsonfile:
        data=json.load(jsonfile)
        for a in data['profile']: 
            username=a['user_name']
            realname=a['real_name']
            country=a['country']
            nb_games=a['nb_games_owned']
            games_id=a['list_of_games']
            playtime_game=a['playtime_game']
    return[username, realname, country, nb_games, games_id, playtime_game]

def get_database():
    url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0002/'
    database_games=requests.get(url)
    database_games=database_games.json()
    return database_games

def destructor_json(database_games,games_id): 
    steam_id=[]
    steam_names=[]
    nb_steam_games=len(database_games['applist']['apps'])
    nb_steam_games=int(nb_steam_games)
    a= 0
    while a<nb_steam_games: 
        steam_id.append(str(database_games['applist']['apps'][a]['appid']))
        steam_names.append(str(database_games['applist']['apps'][a]['name']))
        a=a+1

    games_names=[]
    nb_owned_games=len(games_id)
    nb_owned_games=int(nb_owned_games)
    for e in range(nb_owned_games): 
        if games_id[e] in steam_id :
            indexx = steam_id.index(games_id[e])
            games_names.append(steam_names[indexx])
        else : 
            games_names.append('NaN')
    return games_names

def create_dataframe(name_games, playtime_game): 
    sum_playtime=sum(playtime_game)
    part_playtime=[]
    nb_games=len(name_games)
    nb_games=int(nb_games)
    for k in range(nb_games): 
        pplaytime=(playtime_game[k]/sum_playtime)*100
        part_playtime.append(pplaytime)

    data={'Games' : name_games, 
    'Playtime' : playtime_game, 
    'Part Playtime' : part_playtime}

    df_account=pd.DataFrame(data, columns=['Games', 'Playtime', 'Part Playtime'])
    df_account=df_account.sort_values(['Playtime'], ascending=False)
    return df_account

def save_csv(df):
    df.to_csv('profile_info.csv', index=False)
   
def display_info(name_account, id_account, realname, account_country, nb_owned_games): 
    print('For the account named ', name_account, ':')
    print('The steam id is ', id_account)
    print('The name of the holder is ', realname)
    print('The account is stated in ', account_country)
    print('The owner of the account has ', nb_owned_games, ' games on steam')

def process():
    data_profil=open_data()
    database_games=get_database()
    games_id=data_profil[4]
    games_name=destructor_json(database_games, games_id)
    df_account=create_dataframe(games_name, data_profil[5])
    save_csv(df_account)

process()