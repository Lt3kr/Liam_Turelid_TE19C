K = float(input("konvertera kelvin till celsius: "))

C = K-273

print(f"talet du söker är {C} grader celsius")

c = float(input("nu kan du konvertera celsius till kelvin: "))

k = c+273

print(f"det blir {k} kelvin")

#Eb = engångsbiljeter Mk = månadskort

Eb = 30
Mk = 775

H = float(input("hur mycket åker du?: "))

f = 30*H

if (f >= Mk): {
    print(f"Du borde nog överväga ett månadskort för du ligger på {f}kr och ett månadskort är endast 775kr")
}

else: 
    print(f" det kostar dig {f} kr att åka så mycket")