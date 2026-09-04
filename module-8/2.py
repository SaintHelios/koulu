names = set()
while True:
    meow = input("Enter a name: ")

    if meow != "":
        if meow in names:
            print("Existing name...\n")
        else:
            names.add(meow)
            print("New name...\n")
    elif meow == "":
        break
for i in names:
    print(i)
