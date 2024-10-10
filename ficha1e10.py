kilo = int(input("Indique o seu peso (kg): "))
planet = int(input("Indique o código do planeta: "))

match planet:
    case 1:
        kilo_2 = (kilo*0.37)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 2:
        kilo_2 = (kilo*0.90)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 3:
        kilo_2 = (kilo*0.37)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 4:
        kilo_2 = (kilo*2.53)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 5:
        kilo_2 = (kilo*1.06)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case 6:
        kilo_2 = (kilo*0.91)/0.98
        print("O seu peso no planeta 1 seria de %0.2f" %(kilo_2))
    case _:
        print("O planeta nao esta na lista.")