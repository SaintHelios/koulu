meow = int(input("Syötä vuosiluku: "))

if (meow % 4 == 0 and meow % 100 != 0) or (meow % 400 == 0):
    print("Vuosi on on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")



