from logging import PlaceHolder
from re import X
from dash_core_components.Graph import Graph
from dash_html_components.Data import Data
from dash_html_components.Label import Label
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



app = dash.Dash(__name__) # starten på själva servern

Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "UTF-8") # läser in Regional_Totals_Data.csv filen så datorn kan använda informationen
Gender = pd.read_csv("Gender_Data.csv", encoding = "UTF-8") # läser in Gender_Data.csv filen så datorn kan använda informationen

antaletFallKön = px.bar(Gender, x="Gender", y="Total_Cases", title="Alla antal fall") # detta är själva antaletFallKön statiska grafen som jag kallar på i layouten
dödaKön = px.pie(Gender, values="Total_Deaths", names="Gender", title="Procent av döda män och kvinnor") # detta är den statiska dödakön grafen jag kallar på i layouten

app.layout = html.Div(children=[
    html.H1(children="Welcome to Liams graphs",
    style={
        'textAlign': 'center',
        'color': '#000000'
    }), # endast en text div med styling i

    html.Div(children=''' 
    Skriv in i sökfälten vilka städer du vill jämföra glöm inte att inte stava fel och med stora bokstäver
    '''), # detta är endast en text div
    html.Div([   #Detta är inputfältet som man ska skriva in de städer som man vill ha att jämföra med
        dcc.Input(
        id="stad_1", # själva id:et så informationen kan hämtas
        type='text', # typen av fält
        list='stadVal' # vilken dropdown lista jag vill använda för enkelhetens skull
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

    html.Div(children='''Vad vill du undersöka?'''), # endast en vanlig text div

    dcc.Input( # detta är en text input för att man ska välja vad man vill jämföra
        id="JämförVal",
        type="text",
        list="undersökningVal"
    ),

    dcc.Graph( # detta är den responsiva stapel grafen för valda städer
    id="StadGraf"
    ),

    dcc.Graph( # detta är den responsiva pie grafen för valda städer
        id="StadGraf2"
    ),

    html.Datalist(id='stadVal', children=[ #Skapar en datalist som innehåller förbestämda val som man kan klicka in omedelbart för städer
        html.Option(value='Blekinge'),
        html.Option(value='Dalarna'),
        html.Option(value='Gotland'),
        html.Option(value='Gävleborg'),
        html.Option(value='Halland'),
        html.Option(value='Jämtland Härjedalen'),
        html.Option(value='Jönköping'),
        html.Option(value='Kalmar'),
        html.Option(value='Kronoberg'),
        html.Option(value='Norrbotten'),
        html.Option(value='Skåne'),
        html.Option(value='Stockholm'),
        html.Option(value='Sörmland'),
        html.Option(value='Uppsala'),
        html.Option(value='Värmland'),
        html.Option(value='Västerbotten'),
        html.Option(value='Västernorrland'),
        html.Option(value='Västmanland'),
        html.Option(value='Västra Götaland'),
        html.Option(value='Örebro'),
        html.Option(value='Östergötland')
    ]),

    html.Datalist(id='undersökningVal', children=[ #Skapar en datalist som innehåller förbestämda val som man kan klicka in omedelbart för vad man vill jämföra
        html.Option(label= "antalet döda", value='Total_Deaths'),
        html.Option(label= "antalet fall", value='Total_Cases'),
        html.Option(label= "antal fall per 100k", value='Cases_per_100k_Pop'),
        html.Option(label= "antal ICU", value='Total_ICU_Admissions'),
    ]),

    dcc.Graph( # gör en statisk graf utav antaletFallKön charten
        id= "könsGraf",
        figure = antaletFallKön
    ),

    dcc.Graph( # gör en statisk graf utav dödaKön charten
        id="dödKön",
        figure = dödaKön
    ),

])

@app.callback( # gör en callback för att funktionen ska få alla värden och sedan presenteras
    Output("StadGraf","figure"),
    [Input("stad_1", "value")],
    [Input("stad_2", "value")],
    [Input("stad_3", "value")],
    [Input("stad_4", "value")],
    [Input("JämförVal", "value")]
)

def update_figure(stad_1, stad_2, stad_3, stad_4, JämförVal): # gör en funktion för att det inte ska vara statiska grafer

    städer = [stad_1,stad_2,stad_3,stad_4] # gör en array för enkelhetens skull

    dataframe = Regional[(Regional["Region"].isin([stad_1,stad_2,stad_3,stad_4]))] # skapar en ny dataframe, gör detta av den gamla och använder .isin funktionen för att hitta de val användaren vill ha

    fig = {'data': [dict(x=städer , y = dataframe[JämförVal] ,type="bar")], # skapar en responsiv graf baserad på inputsen av både städer och vad man vill jämföra i form av JämförVal

        'layout':dict(title= "Resultaten: ")}
    return fig

@app.callback( # gör samma callback för den andra funktionen så den tar in samma värden som den andra
    Output("StadGraf2","figure"),
    [Input("stad_1", "value")],
    [Input("stad_2", "value")],
    [Input("stad_3", "value")],
    [Input("stad_4", "value")],
    [Input("JämförVal", "value")]
)

def update_figure2(stad_1, stad_2, stad_3, stad_4, JämförVal): # gör en ny funktion för min pie chart 

    städer = [stad_1,stad_2,stad_3,stad_4] # lägger all städer i en array för atta användas senare i min dataframe och i min graf

    dataframe = Regional[(Regional["Region"].isin([stad_1,stad_2,stad_3,stad_4]))] # Gör ännu en gång en ny dataframe för enkelhetens skull

    fig = go.Figure(data=[go.Pie(labels=städer, values=dataframe[JämförVal])]) # Gör en pie chart som tar in värdena städer som labels och min datatframe med val av JämförVal för values

    return fig


if __name__=="__main__":
    app.run_server(debug=True)


    