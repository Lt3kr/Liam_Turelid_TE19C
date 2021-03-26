import pandas as pd
import numpy as np

df = pd.read_csv("pandachart.csv")

print(df.head(3))
print(df.tail(2))
df = df.fillna(0)
df["Total"] = df.sum(axis=1)
df["Betyg"] = np.where(df["Total"] > 7, "Godkänt", "Underkänt")
df