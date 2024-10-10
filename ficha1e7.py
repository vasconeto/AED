gender = input("Indique o Sexo(M/F): ")
age = int(input("Indique a idade: "))

match gender:
    case "M":
        print(220-age)
    case "F":
        print(226-age)