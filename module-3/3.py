kanta, korkeus = input("Syötä suorakulmion kanta ja korkeus siinä järjestyksessä: ").split()
kanta, korkeus = [int(kanta), int(korkeus)]
piiri = 2 * (kanta + korkeus)
pinta = kanta * korkeus
print("Piiri: {}\nPinta-ala: {}".format(piiri, pinta))
