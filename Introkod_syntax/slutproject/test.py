import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import pandas as pd

Regional = pd.read_csv("Regional_Totals_Data.csv", encoding = "UTF-8")

print(Regional)

input1 = input("")
input2 = input("")

alla = [input1, input2]

df = Regional[(Regional["Region"].isin([input1, input2]))]

print(df)