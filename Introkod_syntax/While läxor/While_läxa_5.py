#gör ett program som använder sig av ett flödesschema
import random


tal = random.randint(1,100) #ger variabeln tal ett random tal från 1-100


n = float(input("thee needs to guess my number from one to one hundred: ")) #frågar efter talet

while n != tal: #när gissningen inte är korrekt så startas while satsen
    if n < tal:
        print(f"Thy are below what I seek, to be specifik you are {tal-n} away") #if satsen kollar om du är under talet och säger även hur långt under
    elif n > tal:
        print(f"Thy are abowe what I seek, to be specifik you are {n-tal} away")
    n = float(input("Now try again: ")) #den här elif satsen gör tvärtom vad if satsen gjorde

print("you are indeed correct") #när while loopen inte längre är aktiv så printas detta


#jag måste tacka Nils i min klass då han hjälpte mig förstå denna uppgift