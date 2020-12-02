a = int(input("Skriv vad du vill ha som a: "))
n = int(input("Skriv vad du vill ha som n: "))
an = int(input("Skriv vad du vill ha som slut a: "))

def summa(a, n, an):
    return(n*(a + an)/2)

print(summa(a,n,an))