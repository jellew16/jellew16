soort =input("/,*,+,-")
delen = "/"
keer = "*"
plus = "+"
min = "-"
if soort == delen:
    num1 = float(input("Nummer 1:"))
    num2 = float(input("Nummer 2:"))
    som1 = num1 / num2
    print(som1)
if soort == keer:
    num3 = float(input("Nummer 1:"))
    num4 = float(input("Nummer 2:"))
    som2 = num3 * num4
    print(som2)
if soort == plus:
    num5 = float(input("Nummer 1:"))
    num6 = float(input("Nummer 2:"))
    som3 = num5 + num6
    print(som3)
if soort == min:
    num7 = float(input("Nummer 1:"))
    num8 = float(input("Nummer 2:"))
    som4 = num7 - num8
    print(som4)
