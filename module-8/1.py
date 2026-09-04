kuukaudet = ("spring", "summer", "autumn", "winter")

kuukausi = int(input("Syötä kuukausi numero: "))

if kuukausi <= 3:
    print("{}".format(kuukaudet[0]))
elif kuukausi <= 6:
    print("{}".format(kuukaudet[1]))
elif kuukausi <= 9:
    print("{}".format(kuukaudet[2]))
elif kuukausi <= 12:
    print("{}".format(kuukaudet[3]))
else:
    print("Error")
