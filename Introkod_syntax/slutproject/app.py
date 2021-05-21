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
#städer = [Sök_efter_stad, Sök_efter_stad2, Sök_efter_stad3, Sök_efter_stad4]
def Rita_allt():
  bool_serie = Regional.Region.isin()
  # print(bool_serie)
  Regional_filter = Regional[bool_serie]
  print(Regional_filter)
  TotalD_bar = px.bar(Regional_filter, x="Region", y="Total_Deaths")
  Cases = px.pie(Regional_filter, names="Cases_per_100k_Pop", values="Cases_per_100k_Pop")
  ICU = px.bar(Regional_filter, x="Region", y="Total_ICU_Admissions")
  TotalD_bar.show()
  Cases.show()
  ICU.show()

app.layout = html.Div(children=[
    html.H1(children="Welcome to Liams graphs",
    style={
        'textAlign': 'center',
        'color': '#000000'
    }),

    html.Div(children='''
    Skriv in i sökfälten vilka städer du vill jämföra glöm inte att inte stava fel och med stora bokstäver
    '''),

    dcc.Graph(
        id= "könsGraf",
        figure = antaletFallKön
    ),

    dcc.Graph(
        id="dödKön",
        figure = dödaKön
    ),

    dcc.Input(
        id="stad_1".format(x),
        type=x,
        PlaceHolder="stad 1".format(x),
        debounce=True
    ),
    dcc.Input(
        id="stad_2".format(x),
        type=x,
        placeholder="stad_2".format(x),
        debounce=True
    ),

    dcc.Input(
        id="stad_3".format(x),
        type=x,
        PlaceHolder="stad_3".format(x),
        debounce=True
    ),

    dcc.Graph(
        id="StadGraf",
    ),

])

@app.callback(
    Output("könsGraf","StadGraf","dödKön"),
    [Input(["stad_1".format(X), "stad_2".format(X), "stad_3".format(X), "stad_4".format(X)], value)]
)

def update_figure(value):
    fig = Rita_allt(value)
    fig.update_layout(transition_duration=500)
    return fig


if __name__=="__main__":
    app.run_server(debug=True)