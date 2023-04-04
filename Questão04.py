num1= int(input("Digite um número positivo ou negativo: "))

if num1 >= 1:
    dobro= num1 * 2
    print("O seu número é positivo, seu dobro é: ", dobro)
elif num1==0:
    print("0 é um número neutro, tente novamente")
else:
    triplo= num1 * 3
    print("O seu número é negativo, seu triplo é:", triplo)