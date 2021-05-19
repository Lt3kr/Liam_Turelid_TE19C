import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc


Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "UTF-8")
Gender = pd.read_csv("Gender_Data.csv", encoding = "UTF-8")

dödaKön = px.pie(Gender, values="Total_Deaths", names="Gender", title="Procent av döda män och kvinnor")
dödaKön.show()

antaletFallKön = px.bar(Gender, x="Gender", y="Total_Cases", title="Alla antal fall")
antaletFallKön.show()

Sök_efter_stad = input("")
Sök_efter_stad2 = input("")
Sök_efter_stad3 = input("")
Sök_efter_stad4 = input("")

total_Cases = 0
Cases_per_100k = 0
total_ICU_Admissions = 0
total_Deaths = 0

städer = [Sök_efter_stad, Sök_efter_stad2, Sök_efter_stad3, Sök_efter_stad4]

def Rita_allt(städer):
  bool_serie = Regional.Region.isin(städer)
  # print(bool_serie)
  Regional_filter = Regional[bool_serie]
  print(Regional_filter)
  TotalD_bar = px.bar(Regional_filter, x="Region", y="Total_Deaths")
  Cases = px.pie(Regional_filter, names="Cases_per_100k_Pop", values="Cases_per_100k_Pop")
  ICU = px.bar(Regional_filter, x="Region", y="Total_ICU_Admissions")
  TotalD_bar.show()
  Cases.show()
  ICU.show()

Rita_allt(städer)