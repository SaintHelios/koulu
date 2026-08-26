meow = "python"
tuah = "rules"
yritykset = 0

rah = str(input("\nSyötä käyttäjätunnus: "))
kah = str(input("Syötä salasana: "))

while rah != meow or kah != tuah:
    print(f"Käyttäjätunnus tai salasana ei täsmää. Yritä uudelleen.\nYritys: {yritykset}\n")
    rah = str(input("Syötä käyttäjätunnus: "))
    kah = str(input("Syötä salasana: "))
    yritykset = yritykset + 1

    if yritykset >= 5:
        print("\n\tPääsy evätty.\n")
        exit()
print("Tervetuloa")
