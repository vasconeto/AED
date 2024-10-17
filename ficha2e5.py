n = int(input("Numero: "))
divisores = 0

if n > 0:
    for i in range (1, n+1):
        if n % i == 0:
            divisores += 1

    if divisores > 2:
        print("O numero %d nao e primo" % (n))
    else:
        print("O numero %d e primo" % (n))

else:
    print("O numero tem de ser maior que 0")