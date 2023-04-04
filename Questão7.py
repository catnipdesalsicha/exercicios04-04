altura= float(input("Digite a sua altura: "))
genero= input("Digite seu sexo: ")
sexo1 = "Feminino", "feminino", "mulher", "Mulher"
sexo2 = "Maculino", "masculino", "homem", "Homem"

if sexo1:
    print("Seu peso ideal de acordo com seu sexo e altura é: ", (62.1*altura)-44.7)

elif sexo2:
    print("Seu peso ideal de acordo com seu sexo e altura é: ", (72.7*altura)-58)