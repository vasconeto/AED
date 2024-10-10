age = int(input("Indique a idade: "))

if age >= 0 and age <= 2:                   #Infancia
    print("Incancia - Primeira Infancia")

elif age >= 3 and age <= 6:                 #Infancia
    print("Incancia - Infancia Intermediaria")

elif age >= 7 and age <= 12:                #Infancia
    print("Incancia - Pre-Adolescencia")

elif age >= 13 and age <= 14:               #Adolescencia
    print("Adolescencia - Puberdade")

elif age >= 15 and age <= 19:               #Adolescencia
    print("Adolescencia - Adolescencia Tardia")

elif age >= 20 and age <= 39:               #Adultez
    print("Adultez - Jovem Adulto")

elif age >= 40 and age <= 59:               #Adultez
    print("Adultez - Meia Idade")

elif age >= 60 and age <= 74:               #Terceira Idade
    print("Terceira Idade - Idosos Jovens")

else:                                       #Terceira Idade
    print("Terceira Idade - Idosos Velhos")

