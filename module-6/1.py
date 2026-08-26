import random

luvut = []
summa = 0

kuutio_maara = int(input("Syötä arpakuutioiden lukumääärä: "))

for i in range(kuutio_maara):
    meow = random.randint(1,6)
    luvut.append(meow)

summa = sum(luvut)
print(f"{summa}")
