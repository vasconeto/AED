kilo = int(input("Peso (kg): "))
height = float(input("Altura (m): "))

imc = kilo/(height**2)

if imc < 18.5:
    print("O seu IMC é: %.2f" % (imc))
    print("Baixo Peso")
elif imc >= 18.5 and imc <= 24.9:
    print("O seu IMC é: %.2f" % (imc))
    print("Peso Normal")
elif imc >= 25 and imc <= 29.9:
    print("O seu IMC é: %.2f" % (imc))
    print("Excesso de Peso")
elif imc >= 30 and imc <= 34.9:
    print("O seu IMC é: %.2f" % (imc))
    print("Obesidade Grau I")
elif imc >= 35 and imc <= 39.9:
    print("O seu IMC é: %.2f" % (imc))
    print("Obesidade Grau II")
else:
    print("O seu IMC é: %.2f" % (imc))
    print("Obesidade Grau III")