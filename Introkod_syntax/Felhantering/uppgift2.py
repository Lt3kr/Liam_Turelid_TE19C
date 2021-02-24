def ar_fyrsiffrigt(tal):
    b = tal//1000
    if b < 10 and b > -10 and b != 0:
        return True
    else:
        return False

    #testprogram
testtal = [100, 231, 10000, 10001, -1000, 102313]

for t in testtal:
    if ar_fyrsiffrigt(t):
        print(f"{t} är fyrasiffrigt")
    else:
        print(f"{t} är inte fyrasiffrigt")