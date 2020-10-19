import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('profile_info.csv')

partition=px.pie(df, values='Part Playtime', names='Games')

app.layout = html.Div(children=[
    html.H1(children="Here is Nda's profile "),



    dcc.Graph(
        id='Partition',
        figure=partition
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)