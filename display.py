import dash
import dash_core_components as dcc
import dash_html_components as html
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
    return partition

df_played=order_data()
partition=graphs(df_played)
 
app.layout = html.Div(children=[
    html.H1(children="Here is Nda's profile "),

    dcc.Graph(
        id='Partition',
        figure=partition
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)