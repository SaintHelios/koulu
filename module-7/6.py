import math

def meow(para, kara):
    r = para / 2
    tuah = math.pi * r ** 2 
    per = tuah / kara
    return per

while True:
    pizza1_halkaisija = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
    pizza1_hinta = float(input("Syötä ensimmäisen pizzan hinta (€): "))

    pizza2_halkaisija = float(input("\nSyötä toisen pizzan halkaisija (cm): "))
    pizza2_hinta = float(input("Syötä toisen pizzan hinta (€): "))
    
    pizza1_suhde = meow(pizza1_halkaisija, pizza1_hinta)
    pizza2_suhde = meow(pizza2_halkaisija, pizza2_hinta)

    if pizza1_suhde > pizza2_suhde:
        print("\nEnsimmäinen pizza antaa paremman vastineen rahalle")
    elif pizza1_suhde < pizza2_suhde:
        print("\nToinen pizza antaa paremman vastineen rahalle")
    elif pizza1_suhde == pizza2_suhde:
        print("\nMolemmat antavat saman verran vastinetta") 
    break

