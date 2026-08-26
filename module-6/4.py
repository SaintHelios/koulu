kaupungit = []
counter = 0

for x in range(5):
    meow = str(input(f"Syötä kaupungin nimi {counter}/5: "))
    counter = counter + 1
    kaupungit.append(meow)

for i in kaupungit:
    print(f"\t{i}")
