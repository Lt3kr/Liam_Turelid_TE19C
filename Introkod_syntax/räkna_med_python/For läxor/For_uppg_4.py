#beräkna flöjande aritmetiska summa 1+3+5...+ 99
s = 1
for i in range(100):
    s += 2*i-1
    print(s)