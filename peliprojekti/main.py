
def mako():
    lista = []
    meow = input("Syötä esine")
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
    komento = str(input("\nKomennot:\n\t(1) Tulosta nimi\n\t(2) Tulosta ikä\nSyötä komento: "))
    if komento == "1":
        print(f"\t{nimi}")
    elif komento == "2":
        print(f"\t{ika}")
    elif komento == "lopeta":
        print("Lopetetaan...")
        exit()
    else:
        print("\tVirheellinen komento.")
