import pandas as pd
import matplotlib.pyplot as plt

Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "ISO-8859-1")
Gender = pd.read_csv("Gender_Data.csv", encoding = "ISO-8859-1")

Sök_efter_stad = input("")
Sök_efter_stad_2 = input("")
Sök_efter_stad_3 = input("")
Sök_efter_stad_4 = input("")

Män = 0
Kvinnor = 0

Män = Gender[Gender["Gender"] == "Male"]
Män = Män["Total_Cases"].sum()

Kvinnor = Gender[Gender["Gender"] == "Kvinnor"]
Kvinnor = Kvinnor["Total_Cases"].sum()

print(Män)

total_Cases = []
Cases_per_100k = []
total_ICU_Admissions = []
total_Deaths = []

