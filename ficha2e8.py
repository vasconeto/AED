n = int(input("Indique o numero: "))

if 1 <= n <= 99:
    representacao_binaria = ""
    
    while n > 0:
        resto = n % 2
        representacao_binaria = str(resto) + representacao_binaria
        n = n // 2  

    print("A representação em binário de %d é: %s" % (n, representacao_binaria))
else:
    print("Número fora do intervalo permitido.")

