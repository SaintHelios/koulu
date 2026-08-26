import random
meow = random.randint(1, 10) 
tuah = int(input("Syötä lukuarvaus väliltä 1-10. Ohjelma avustaa sinua kertomalla, onko luku liian suuri vai liian pieni.\nSyötä arvaus: "))

while tuah != meow:
    if tuah > meow:
        print("Liian suuri arvaus")
    elif tuah < meow:
        print("Liian pieni arvaus")    
    else:
        break
    tuah = int(input("Toinen yritys: "))
    
print("Arvauksesi on oikein!")

