# uppgift 5a

for f in range (11):
    print(f"{5*f}", end=" ")
print()

#uppgift 5b

k = int(input("ge mig ett tal! "))
for n in range(11):
    print(f"{k*n}", end=" ")
print()

#uppgift 5c
for j in range(11): #gör vad som står under 10 ggr
    for i in range(11): #gör samma här
        print(f"{i*j}", end = " ") #tar j och gångrar det med varje i för att sedan printa det
    print()


#detta är hela uppgift 5