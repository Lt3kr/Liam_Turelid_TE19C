# gör en funk som beräknar s = 1 + 3 + 5 + 7 + 9 + ... + (2n +1)

Start = int(input("Skriv vad starten är: ")) - 1
n = int(input("Skriv vad du vill ha som den sista delen: "))


def Aritmetisk_summa(n):

    Summan = 0

    for x in range(Start, n+1):
        Summan += (2*x + 1)
    return Summan
    

print(f"den aritmetiska summan av det du har givit är {(Aritmetisk_summa(n))} vilket alltså är {Start} + {Start+1} + {Start+3}+ ... enda tills slutet vilket är {2*n + 1}")

# hela uppgift 2