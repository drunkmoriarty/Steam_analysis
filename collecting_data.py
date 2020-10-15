import pandas as pd
import requests 
import html
import json
import re

key_api='KEY_API'

def get_name_account(): 
    name_account=input("In order to get infos about an account, please enter the name of the account: ")
    return name_account

def scrapper(url, pattern): 
    website=requests.get(url)
    website=website.text
    website=html.unescape(website) 
    website=website.replace('\n','')
    website=website.replace('\t','')
    website=website.replace('\r','')
    results=re.findall(pattern, website)
    return results

def get_id(name_account): 
    url='https://steamidfinder.com/lookup/'+name_account
    pattern_id='<br>steamID64: <code>(.+?(?=</code>))'
    id_account=scrapper(url, pattern_id)
    if not id_account:
        id_account='NaN'
        print('This account does not exist. Please try again.')
        return id_account
    else :
        id_account=id_account[0]
        return id_account
            
def loop_name(): 
    i=0
    while i<1 : 
        name_account=get_name_account()
        id_account=get_id(name_account)
        if id_account=='NaN': 
            i=0
        else :
            i=1
            return [name_account, id_account]

def get_info_profil(key, id_account): 
    url= "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="+key+"&steamids="+id_account+'&format=json'
    info=requests.get(url)
    info_profil=info.json()
    return info_profil

def get_profil_games(key, id_account):
    url='http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key='+key+'&steamid='+id_account+'&format=json'
    info=requests.get(url)
    info_games=info.json()
    return info_games   

def get_data_profil(info_profil): 
    realname=info_profil['response']['players'][0]['realname']
    account_country=info_profil['response']['players'][0]['loccountrycode']
    return [realname, account_country]

def get_data_profil_games(info_games): 
    games_id=[]
    playtime_game=[]
    if not info_games['response']:
        nb_owned_games= 'a private profil. No information about their games could be retrieved'
        return [nb_owned_games, games_id, playtime_game]
    else : 
        nb_owned_games=info_games['response']['game_count']
        nb_owned_games=int(nb_owned_games)
        for i in range(nb_owned_games):
            id_game=str(info_games['response']['games'][i]['appid'])
            games_id.append(id_game)
            playtime_game.append(info_games['response']['games'][i]['playtime_forever'])
        return [nb_owned_games, games_id, playtime_game]

def raw_dataframe(games_id, playtime_game): 
    data={'Game Id' : games_id, 
    'Playtime': playtime_game}
    data=pd.DataFrame(data, columns=['Game Id', 'Playtime'])
    data=data.sort_values(by=['Playtime'], ascending=False)
    return data

def json_file(name_account, id_account, real_name, country, nb_games_owned, list_games_owned, playtime_game):
    info={}
    info['profile']=[]
    info['profile'].append({
        'user_name' : name_account, 
        'id_profil' : id_account, 
        'real_name' : real_name, 
        'country' : country, 
        'nb_games_owned': nb_games_owned, 
        'list_of_games' : list_games_owned,
        'playtime_game' : playtime_game
    })
    with open('data_profil_'+name_account+'.', 'w') as jsonfile:
        json.dump(info, jsonfile)
    print(info)

def process():
    detail_profil=loop_name()
    info_profil=get_info_profil(key_api, detail_profil[1])
    profil_info=get_data_profil(info_profil)
    info_games=get_profil_games(key_api, detail_profil[1])
    owned_games=get_data_profil_games(info_games)
    json_file(detail_profil[0], detail_profil[1], profil_info[0], profil_info[1], owned_games[0], owned_games[1], owned_games[2])

process()