import random

while True:
    num = random.randint(1,50)
    n = int(input("Tentativa: "))
    attem = 1

    while attem < 11 and n != num:
        if n > num:
            print("Numero e MENOR.")
        elif n < num:
            print("Numero e MAIOR.")
    
        attem += 1
        if attem < 11:
            n = int(input("Tentativa: "))
    
    if n == num:
        print("Acertou! Em %d tentativas" % (attem))
    else:
        print("Esgotou as 10 tentativas :(")

    new = input("Novo jogo (S/N)? ")
    if new == "N":
        break
    elif new != "S":
        print("Indique um valor correto")
    
    