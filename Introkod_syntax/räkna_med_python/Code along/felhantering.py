while True:
    try:
        ålder = float(input("Hur gammal är du? "))
        assert ålder >= 0 and ålder < 125, "Din ålder ska vara mellan 0 och 124"
        break
    except AssertionError as msg:
        print(msg)
    except:
        print("Ålder ska vara ett tal inte en sträng")


if ålder >= 18:
    print("Du är vuxen")
else:
    print("Du är barn")