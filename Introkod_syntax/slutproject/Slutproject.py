import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "ISO-8859-1")
Gender = pd.read_csv("Gender_Data.csv", encoding = "ISO-8859-1")

dödaKön = px.pie(Gender, values="Total_Deaths", names="Gender", title="Procent av döda män och kvinnor")
dödaKön.show()

antaletFallKön = px.bar(Gender, x="Gender", y="Total_Cases", title="Alla antal fall")
antaletFallKön.show()

Sök_efter_stad = input("")
Sök_efter_stad2 = input("")
Sök_efter_stad3 = input("")
Sök_efter_stad4 = input("")

allaStäder = [Sök_efter_stad, Sök_efter_stad2, Sök_efter_stad3, Sök_efter_stad4]

total_Cases = []
Cases_per_100k = []
total_ICU_Admissions = []
total_Deaths = []

def hitta_Stad(allaStäder):
  Hitta1 = Regional[Regional["Region"] == allaStäder[0]]
  Hitta2 = Regional[Regional["Region"] == allaStäder[1]]
  Hitta3 = Regional[Regional["Region"] == allaStäder[2]]
  Hitta4 = Regional[Regional["Region"] == allaStäder[3]]

  Fall1 = Hitta1["Total_Cases"].sum()
  Fall2 = Hitta2["Total_Cases"].sum()
  Fall3 = Hitta3["Total_Cases"].sum()
  Fall4 = Hitta4["Total_Cases"].sum()

  total_Cases = [Fall1, Fall2, Fall3, Fall4]

print(hitta_Stad(total_Cases))
