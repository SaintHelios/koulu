inches = float(input("Syötä tuumamäärä.\nNegatiivinen luvut keskeyttävät ohjelman.\n"))
while inches >= 0:
    cm = inches * 2.54
    print("{}cm\n".format(cm))
    inches = float(input("Toinen luku: "))
        
