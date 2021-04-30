import pandas as pd
import matplotlib.pyplot as plt

Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "ISO-8859-1")
Gender = pd.read_csv("Gender_Data.csv", encoding = "ISO-8859-1")



Män = 0
Kvinnor = 0

Män = Gender[Gender["Gender"] == "Male"]
Män = Män["Total_Cases"].sum()

Kvinnor = Gender[Gender["Gender"] == "Kvinnor"]
Kvinnor = Kvinnor["Total_Cases"].sum()

print(Män)

totalCase = []

total_Cases = []
Cases_per_100k = []
total_ICU_Admissions = []
total_Deaths = []

def hitta_Stad(Sök_efter_stad, Sök_efter_stad2, Sök_efter_stad3, Sök_efter_stad4):
  Hitta1 = Regional[Regional["Region"] == Sök_efter_stad]
  Hitta2 = Regional[Regional["Region"] == Sök_efter_stad2]
  Hitta3 = Regional[Regional["Region"] == Sök_efter_stad3]
  Hitta4 = Regional[Regional["Region"] == Sök_efter_stad4]

  Hitta1 = Hitta1["Total_Cases"].sum()
  Hitta2 = Hitta2["Total_Cases"].sum()
  Hitta3 = Hitta3["Total_Cases"].sum()
  Hitta4 = Hitta4["Total_Cases"].sum()

  totalCase = [Hitta1, Hitta2, Hitta3, Hitta4]

print(hitta_Stad(totalCase))