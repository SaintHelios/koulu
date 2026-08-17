x, y, z = input("Syötä kolme numeroa peräkkäin. Ohjelma tulostaa niiden lukujen summan, tulon ja keskiarvon.\n:").split()
x, y, z = [int(x), int(y), int(z)]
summa = x + y + z
tulos = x * y * z 
keskiarvo = (x+y+z) / 3
print("Summa: {}\nTulos: {}\nKeskiarvo: {}".format(summa, tulos, keskiarvo))

