with open("Provresultat.txt", "r") as f1:
    a = sorted(open("Provresultat.txt"))

#with open("Provresultat.txt", "a") as f2:
    #f2.write("\n")
    #for name in a:
        #f2.write(str(name))

with open("Provresultat.txt", "a") as f3:
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    for gamer in a:
        names = gamer.split("\n")
        poäng = int(names[-2:])
        if poäng < 20:
            F.append(names)
        elif poäng < 30:
            E.append(names)
        elif poäng < 40:
            D.append(names)
        elif poäng < 50:
            C.append(names)
        elif poäng < 60:
            B.append(names)
        elif poäng < 70:
            A.append(names)
    f3.write("\n" + "F:" + "\n" + str(F) + "\n" + "E:" + "\n"+ str(E) + "\n" + "D:" + "\n" + str(D) + "\n" + "C:" + "\n" + str(C) + "\n" + "B:" + "\n" + str(B) + "\n" + "A:" + "\n" + str(A))


