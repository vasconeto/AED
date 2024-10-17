import random

num = random.randint(1,50)
n = int(input("Tentativa: "))
attem = 1

while attem < 11 and n != num:
    if n > num:
        print("Numero e menor.")
    elif n < num:
        print("Numero e maior.")
    
    attem += 1
    if attem < 11:
        n = int(input("Tentativa: "))
    
if n == num:
    print("Acertou! Em %d tentativas" % (attem))
else:
    print("Esgotou as 10 tentativas :(")