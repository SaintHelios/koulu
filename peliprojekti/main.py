lista = []

def mako():
    meow = input("Syötä esine: ")
    lista.append(meow)
    return lista

def print_lista(lista):
    for i in lista:
        print(i)
def woof():
    print("meow")

nimi = input("Kerro Nimesi: ")
ika = int(input("Kerro ikäsi: "))

if ika < 12:
    print("Pelaaja on ala-ikäinen (alle 12v). Peli keskeytyy...")
    exit()
print(f"Terve, {nimi}")

while True:
    komento = str(input("\nKomennot:\n\t(lopeta) Sulkeee ohjelman\n\t(1) Syötä esineen listaan\n\t(2) Tulostaa listan esineitä\nSyötä komento: "))
    if komento == "1":
        mako()
    elif komento == "2":
        print_lista(lista)
    elif komento == "lopeta":
        print("Lopetetaan...")
        exit()
    else:
        print("\tVirheellinen komento.")
