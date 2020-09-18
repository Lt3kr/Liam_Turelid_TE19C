vinkel = float(input("ange en vinkel i grader, där 0 <= v <= 360: "))

# 0 <= v < 90 spetsig
# trubbig 90 < v < 180

if vinkel >= 0 and vinkel < 90:
    print("spetsig")
elif vinkel == 90:
    print("Rät vinkel")
elif vinkel > 90 and vinkel < 180:
    print("Trubbig vinkel")
elif vinkel == 360:
    print("Den är rund!")
elif vinkel == 180:
    print("Den är ju rak!")
else:
    print("Konvex vinkel")