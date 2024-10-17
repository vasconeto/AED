n = int(input("Nº de termos a imprimir: "))

if n <= 0:
    print("Numero tem de ser maior que 0.")
else:
    fibonacci = [0, 1]
    
    if n == 1:
        print("Os primeiros %d termos da sequência de Fibonacci são: [0]" % (n))
    else:
        for i in range(2, n):
            next_term = fibonacci[i-1] + fibonacci[i-2]
            fibonacci.append(next_term)
        
        print("Os primeiros %d termos da sequência de Fibonacci são: %s" % (n, fibonacci[:n]))

