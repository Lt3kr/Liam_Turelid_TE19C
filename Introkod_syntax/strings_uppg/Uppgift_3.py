Skriv = input("skriv något utan mellanslag: ")

kontrolator = Skriv.split(" ")

print(f"Längden är {Skriv.__len__()}")

Skriv2 = kontrolator.upper()
if Skriv2[::-1] == Skriv2:
    print("Det är ett palindrom")