print("Planetas")
print("1 - Mercurio")
print("2 - Venus")
print("3 - Marte")
print("4 - Jupiter")
print("5 - Saturno")
print("6 - Urano")

kilo = int(input("Indique o seu peso (kg): "))          #Peso
planet = int(input("Indique o código do planeta: "))    #Planeta

match planet:
    case 1:                                     #Mercurio
        kilo_2 = (kilo*0.37)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 2:                                     #Venus
        kilo_2 = (kilo*0.90)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 3:                                     #Marte
        kilo_2 = (kilo*0.37)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 4:                                     #Jupiter
        kilo_2 = (kilo*2.53)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 5:                                     #Saturno
        kilo_2 = (kilo*1.06)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 6:                                     #Urano
        kilo_2 = (kilo*0.91)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case _:
        print("O planeta nao esta na lista.")