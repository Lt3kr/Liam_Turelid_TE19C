
EttOrd = input("ge mig ett ord utan mellanslag så ska jag se om det är palindrom eller inte: ")

palindromKontrolant = EttOrd.upper()

if palindromKontrolant[::-1] == palindromKontrolant:
    print("Det är ett palindrom")