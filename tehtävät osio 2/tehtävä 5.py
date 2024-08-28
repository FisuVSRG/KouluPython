leiviska = 8512
naula = 425.6
luoti = 13.3
gramma = 1
leiviskaMaara = float(input("Anna leiviskät."))
naulaMaara = float(input("Anna naulat."))
luotiMaara = float(input("Anna luodit."))
paino = ((leiviska * leiviskaMaara) + (naula * naulaMaara) + (luotiMaara * luoti))
kilogrammat = paino // 1000
grammat = paino % 1000
print(f"Massa nykymittojen mukaan: {kilogrammat:.0f} kilogrammaa ja {grammat:.2f} grammaa.")