# gör en funk som beräknar s = 1 + 2 + 3 + 4 + (2n +1)

a = int(input("antal repitioner: "))
b = int(input("ge mig startvärdet: "))

def artimetiskSumma(a):
    return (b + a*2)

print(f"den aritmetiska summan av det du har givit är {artimetiskSumma(a)}")

# hela uppgift 2