# Steam_analysis

*Steam_analysis is a complete data analysis' project composed by three parts : collecting the data by making calls to steam's API, making a clean database in python and its visualisation.*

## 📁 Collecting data
In order to make calls to Steam's API, the **account id** for the profile is required. The app asks the user for the name of the account and collects the account id by scrapping a [Finder ID website](https://steamidfinder.com/). 
The app is collecting **2 sorts of data** : 
- about the **profil** *(real name, country)*, 
- about the **owned games** *(how much games are owned by the account, games' id and playtime per game)*. 

The collected data is then stored in a json file. 

## 🧾 Data Processing
This part focuses on **cleaning the collected data** and retrieve for each game its name. The information is displayed in a dataframe : game's name, playtime in minutes, part of this game in the total playtime (in percent). The dataframe is then saved in a csv file. 


## 📈 Displaying data
The final result is based on the sketch shown below. The app displays the collected data about the account : 
- a text for profil's information
- a pie chart of the playtime's distribution per game
- a table for the 10 most played games. 

![Final version Sketch](https://i.imgur.com/wL6NPGv.png)
