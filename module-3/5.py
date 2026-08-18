leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("\nAnna naulat.\n"))
luodit = float(input("\nAnna luodit.\n"))

yhteensa_luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
yhteensa_grammat = yhteensa_luodit * 13.3

kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000

print("\nMassa nykymittojen mukaan:\n{} kilogrammaa ja {:.2f} grammaa".format(kilogrammat, grammat))
