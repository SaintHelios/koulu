import random

rah = int(input("Syötä nopan maksimisilmäluku: "))

def tuah(rah):
    tuah = random.randint(1,rah)
    return tuah

while True:
    meow = tuah(rah)
    if meow != rah:
        print(meow)
    elif meow == rah:
        print(meow)
        break
