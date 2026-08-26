import random

def tuah():
    tuah = random.randint(1,6)
    return tuah

while True:
    meow = tuah()
    if meow != 6:
        print(meow)
    elif meow == 6:
        print(meow)
        break
