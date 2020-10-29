import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def open_data():
    with open('data_profil.json', 'r') as jsonfile:
        data=json.load(jsonfile)
        for a in data['profile']: 
            username=a['user_name']
            realname=a['real_name']
            country=a['country']
            nb_games=str(a['nb_games_owned'])
            playtime_game=str(round((sum(a['playtime_game']))/60))
    return[username, realname, country, nb_games, playtime_game]

def order_data():
    df = pd.read_csv('profile_info.csv')
    df_played=df[df.Playtime != 0]
    return df_played

def graphs(df) :
    partition=px.pie(df, values='Part_Playtime', names='Games')

    table=go.Figure(data=[go.Table(header=dict(values=list(df.columns), line_color='darkslategray', align='center'),
            cells=dict(values=[df.Games, df.Playtime, df.Playtime_Hours, df.Part_Playtime], line_color='darkslategray',align='center'))
            ])
    return [partition, table]

data_profil=open_data()
df_played=order_data()
partition=graphs(df_played)
 
app.layout = html.Div([
    html.H1(children="Here is "+ data_profil[0] +"'s profile"),

    html.Div([
        html.P(' This is a work in progress made by Maria Rasskazova (mrasska).'),
        html.P('More info : https://github.com/mrasska/Steam_analysis')
        ]
    ),

     html.Div([
        html.P("Username: " + data_profil[0]),
        html.P("Real name: " + data_profil[1]), 
        html.P("Country: "+ data_profil[2]),
        html.P("Number of games owned: " + data_profil[3]), 
        html.P("Total playtime:  "+ data_profil[4] + " hours"), 
        ]
    ),

    dcc.Graph(figure=partition[0]), 

    dcc.Graph(figure=partition[1])
])

if __name__ == '__main__':
    app.run_server(debug=True)