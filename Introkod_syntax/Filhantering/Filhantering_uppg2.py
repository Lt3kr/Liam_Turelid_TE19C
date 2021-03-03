with open("Provresultat.txt", "r") as f1:
    a = sorted(f1)

with open("Provresultat.txt", "a") as f2:
    for i in f2:
        f2.write(str(a))
        f2.write("\n")


