Skriv = input("skriv något utan mellanslag: ")

kontrolator = Skriv.split(" ").__len__()

if kontrolator > 1:
    print("vad var det jag sa?!")
else:
    print(f"Längden är {Skriv.__len__()}")

Skriv2 = Skriv.upper()
if Skriv2[::-1] == Skriv2:
    print("Det är ett palindrom")