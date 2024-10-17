terms = int(input("Quantos números tem a lista: "))

mai = 0  
sec = 0  

for i in range(terms):
    n = int(input("Número: ")) 

    if n > mai:             
        mai = n    
    elif n > sec and n != mai:
        sec = n    

if sec == 0:
    print("Não há um segundo maior número.")
else:
    print("O segundo maior valor da lista de numeros lidos é: %d" % sec)
