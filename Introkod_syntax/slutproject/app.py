from logging import PlaceHolder
from re import X
from dash_core_components.Graph import Graph
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "UTF-8")
Gender = pd.read_csv("Gender_Data.csv", encoding = "UTF-8")

#Sök_efter_stad = input("")
#Sök_efter_stad2 = input("")
#Sök_efter_stad3 = input("")
#Sök_efter_stad4 = input("")

antaletFallKön = px.bar(Gender, x="Gender", y="Total_Cases", title="Alla antal fall")
dödaKön = px.pie(Gender, values="Total_Deaths", names="Gender", title="Procent av döda män och kvinnor")
städer = []
def Rita_allt(städer):
  bool_serie = Regional.Region.isin(städer)
  # print(bool_serie)
  Regional_filter = Regional[bool_serie]
  print(Regional_filter)
  TotalD_bar = px.bar(Regional_filter, x="Region", y="Total_Deaths")
  Cases = px.pie(Regional_filter, names="Cases_per_100k_Pop", values="Cases_per_100k_Pop")
  ICU = px.bar(Regional_filter, x="Region", y="Total_ICU_Admissions")


input_types = ['text', 'text', 'text', 'text']

app.layout = html.Div(children=[
    html.H1(children="Welcome to Liams graphs",
    style={
        'textAlign': 'center',
        'color': '#000000'
    }),

    html.Div(children='''
    Skriv in i sökfälten vilka städer du vill jämföra glöm inte att inte stava fel och med stora bokstäver
    '''),
    html.Div([   #Detta är inputfältet som man ska skriva in de städer som man vill ha
        dcc.Input(
        id="stad_1",
        type='text',
        list='stadVal'
        ),
        dcc.Input(
        id="stad_2",
        type='text',
        list='stadVal'
        ),
        dcc.Input(
        id="stad_3",
        type='text',
        list='stadVal'
        ),
        dcc.Input(
        id="stad_4",
        type='text',
        list='stadVal'
        )
    ]),

    html.Datalist(id='stadVal', children=[ #Skapar en datalist som innehåller förbestämda val som man kan klicka in omedelbart
        html.Option(value='Blekinge'),
        html.Option(value='Dalarna'),
        html.Option(value='Gotland'),
        html.Option(value='Gävleborg')
    ]),

    dcc.Graph(
        id= "könsGraf",
        figure = antaletFallKön
    ),

    dcc.Graph(
        id="dödKön",
        figure = dödaKön
    ),

])

@app.callback(
    Output("könsGraf","dödKön"),
    [Input("stad_1", "value")],
    [Input("stad_2", "value")],
    [Input("stad_3", "value")],
    [Input("stad_4", "value")]
)

# def update_figure(stad_1, stad_2, stad_3, stad_4):
    # Välja = [stad_1, stad_2, stad_3, stad_4]
    # bool_serie = Regional.Region.isin(Välja)
    # print(bool_serie)
    # Regional_filter = Regional[bool_serie]
    # TotalD_bar = px.bar(Regional_filter, x="Region", y="Total_Deaths")
    # fig = TotalD_bar
    # return fig

def update_figure(stad_1, stad_2, stad_3, stad_4):
    fig = make_subplots(rows=1, cols=3)

    fig.add_trace(go.Bar(y=[], x=[stad_1, stad_2, stad_3, stad_4]))

if __name__=="__main__":
    app.run_server(debug=True)