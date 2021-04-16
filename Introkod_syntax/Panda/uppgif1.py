# sysselsättning del a)
# import pandas as pd 
# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# ef = df[df["sysselsättning"] == "förvärvsarbetande"] 
# summa = ef["2019"].sum()
# print(summa)


# b)
# import pandas as pd 
# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# ef = df[df["sysselsättning"] == "ej förvärvsarbetande"] 
# summa = ef["2019"].sum()
# print(summa)

# c)
# import pandas as pd
# import matplotlib.pyplot as plt

# sum1 = 0
# sum2 = 0

# df = pd.read_csv("sysselsattning.csv", encoding = "ISO-8859-1", header=1)
# sum1 = df[df["sysselsättning"] == "förvärvsarbetande"]
# sum2 = df[df["sysselsättning"] == "ej förvärvsarbetande"]
# sum1 = sum1["2019"].sum()
# sum2 = sum2["2019"].sum()

# förv = [sum1, sum2]
# labels = ["förvärvsarbetande","ej förvärvsarbetande"]
# plt.pie(förv, labels = labels, autopct="%1.1f%%")
# plt.title("andel av förvärvsarbetande och ej")
# plt.show