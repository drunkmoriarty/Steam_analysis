import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def order_data():
    df = pd.read_csv('profile_info.csv')
    df_played=df[df.Playtime != 0]
    return df_played

def graphs(df) :
    partition=px.pie(df, values='Part_Playtime', names='Games')

    table=go.Figure(data=[go.Table(header=dict(values=list(df.columns), line_color='darkslategray', align='center'),
            cells=dict(values=[df.Games, df.Playtime, df.Part_Playtime], line_color='darkslategray',align='center'))
            ])
    return [partition, table]


df_played=order_data()
partition=graphs(df_played)
 
app.layout = html.Div(children=[
    #html.H1(children="Here is "+ username +'s profile "),

    html.Div(children='''
        This is a work in progress made by Maria Rasskazova (drunkmoriarty). 
        <br>
        More info : https://github.com/drunkmoriarty/Steam_analysis
    '''),

    dcc.Graph(figure=partition[0]), 

    dcc.Graph(figure=partition[1])
])

if __name__ == '__main__':
    app.run_server(debug=True)