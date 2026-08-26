meow = int(input("Syötä kokonaisluku: "))

if meow <= 1:
    print(f"{meow} ei ole alkuluku")
else:
    alkuluku = True

    for i in range(2, meow):
        if meow % i == 0:
            alkuluku = False
            break
    if alkuluku:
        print(f"{meow} on alkuluku")
    else:
        print(f"{meow} ei ole alkuluku")
