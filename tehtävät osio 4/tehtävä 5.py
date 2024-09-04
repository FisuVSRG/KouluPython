tunnus = "Python"
salasana = "rules"
kerrat = 1
while kerrat <= 5:
    inputTunnus = input("Tunnus: ")
    inputSalasana = input("Salasana: ")
    if inputTunnus != tunnus or inputSalasana != salasana:
        print("Väärin.")
        kerrat = kerrat + 1
    elif inputTunnus == tunnus and inputSalasana == salasana:
        print("Tervetuloa.")
        break
if kerrat > 5:
    print("Pääsy evätty.")