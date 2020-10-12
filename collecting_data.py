import requests 
import html
import json
import re

key_api='1830A7ABA911AB6BD53DED70F1683CE1'

#The main goal of this app is to create an interactive interface where someone puts the name of an account and the app gives back information about it. 
#The user can download the data (csv file) and iterate the action without relaunching the app. 

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
        print('This account does not exist. Please try again.')
    else:
        id_account=id_account[0]
    return id_account

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
    if not info_games['response']:
        print("This account is private, data couldn't be retrieved.")
        nb_owned_games= 'Private profil. No information'
        return nb_owned_games
    else : 
        nb_owned_games=info_games['response']['game_count']
        return nb_owned_games

def display_info(name_account, id_account, realname, account_country, nb_owned_games): 
    print('For the account named ', name_account, ':')
    print('The steam id is ', id_account)
    print('The name of the holder is ', realname)
    print('The account is stated in ', account_country)
    print('The owner of the account has ', nb_owned_games, ' games on steam')

def process():
    name_account=get_name_account()
    id_account=get_id(name_account)
    info_profil=get_info_profil(key_api, id_account)
    profil_info=get_data_profil(info_profil)
    info_games=get_profil_games(key_api, id_account)
    owned_games=get_data_profil_games(info_games)
    display_info(name_account, id_account, profil_info[0], profil_info[1], owned_games)
    
process()