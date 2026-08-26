meow = []
kah = 0
while True:
    tuah = input("Syötä luku: ")

    if tuah != "":

        try:
            luku = int(tuah)
            meow.append(luku)
        except ValueError:
            print("Virheellinen syöttö.\n")
    else:
        break
meow.sort(reverse=True)
for i in meow[:5]:
    print(i)
