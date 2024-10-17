infe = int(input("Indique o limite Inferior: "))
supe = int(input("Indique o limite Superior: "))
soma = 0

for i in range(infe, supe+1):
    if i % 2 == 0:
        soma += i
    
print(soma)