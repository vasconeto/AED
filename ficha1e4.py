kilo = int(input("Peso (kg): "))
height = float(input("Altura (m): "))

imc = kilo/(height**2)

print("O seu IMC é: %.2f" % (imc))