luvut = []

while True:
    syote = input("Syötä luku: ")

    if syote == "":
        break
    luvut.append(syote)
if luvut:
    suurin = max(luvut)
    pienin = min(luvut)
    print(f"Suurin: {suurin}\nPienin: {pienin}")
else:
    print("meow")
