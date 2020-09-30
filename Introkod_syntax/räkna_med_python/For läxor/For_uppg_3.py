# skriv ett program som beräknar följande aritmetiska summa med hjälp av for-satser: s = 1 + 2 + 3 ... + 100

s = 0
for i in range(101):
    s += i
    print(s)