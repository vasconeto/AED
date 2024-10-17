n = int(input("Indique o numero: "))
soma = 0

for i in range(1, n):
    if n%i == 0:
        soma += i
    else:
        continue
    
if soma == n:
    print("O numero e perfeito")
else:
    print("O numero nao e perfeito")