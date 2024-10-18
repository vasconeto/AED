n = int(input("Number: "))
soma = 1

if n == 0:
    print("Fatorial de 0 é 1")
else:
    for i in range(1, n+1):
        soma *= i

print("O fatorial de %d é %d." % (n, soma))
