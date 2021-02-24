Månadskort = 100
engångsbiljet = 25


while True:
    try: 
        kollapris = int(input("Hur många gånger åker du per månad?: "))
        assert kollapris > 1 and kollapris < 1000, "Tror inte du åker mer än 1000 ggr per månad och det är meningslöst att kolla om du ändå inte tänker åka"
        break
    except AssertionError as message:
        print(message)
    except:
        print("Endast siffror!")
    
if kollapris*engångsbiljet < Månadskort:
     print("engångsbiljet är nog bäst för dig")
else:
    print("Du borde nog skaffa månadskort")



    

