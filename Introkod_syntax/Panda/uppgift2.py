# a)
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# ef = df[df["sysselsättning"] == "förvärvsarbetande"]
# män = ef[ef["kön"] == "män"]["2019"].sum()

#b)

# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# ef = df[df["sysselsättning"] == "förvärvsarbetande"]
# kvinnor = ef[ef["kön"] == "kvinnor"]["2019"].sum()

#c)

# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# ef = df[df["sysselsättning"] == "ej förvärvsarbetande"]
# ej_män = ef[ef["kön"] == "män"]["2019"].sum()

#d)

# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# ef = df[df["sysselsättning"] == "ej förvärvsarbetande"]
# ej_kvinnor = ef[ef["kön"] == "kvinnor"]["2019"].sum()

#e)

#label = ["Män förs.", "Män ej förs.", "Kvinnor förs.", "Kvinnor ej förs."]
#värde = [män, ej_män, kvinnor, ej_kvinnor]
#x_axel = np.arange(len(label))

#plt.title("Förvärvsarbetande")
#plt.ylabel("Miljoner")
#plt.bar(x_axel, värde)
