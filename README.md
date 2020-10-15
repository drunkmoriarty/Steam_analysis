# Steam_analysis

*Steam_analysis is a complete data analysis' project composed by three parts : collecting the data by making calls to steam's API, making a clean database in python and its visualisation.*

## 📁 Collecting data
In order to make calls to Steam's API, the **account id** for the profile is required. The app asks the user for the name of the account and collects the account id by scrapping a [Finder ID website](https://steamidfinder.com/). 
The app is collecting **2 sorts of data** : 
- about the **profil** *(realname, country)*, 
- about the **owned games** *(how much games is owned by the account, games' id and playtime per game)*. 

The collected data is then stored in a json file. 
