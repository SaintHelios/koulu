kuha = int(input("Syötä kuhan pituus senttimetreinä (cm): "))

if kuha < 37: 
    meow = 37 - kuha
    print(f"Kuhan pituus on {meow}cm alimittainen. Laske kuha takaisin järveen.")
else:
    print("Kuhan pituus on sopiva.")
