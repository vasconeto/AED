gender = input("Indique o Sexo(M/F): ")
height = int(input("Indique a altura: "))

match gender:
    case "M":
        print((height-100) - (height-150)/4)
    case "F":
        print((height-100) - (height-150)/2)
            