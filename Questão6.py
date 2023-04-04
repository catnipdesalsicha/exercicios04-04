num1= int(input("Digite um valor: "))
num2= int(input("Digite outro valor diferente: "))
num3= int(input("Digite mais um valor diferente: "))


if num1 < num2 < num3:
    print("Aqui estão os valores em ordem decrescente:")
    print(num3, num2, num1)

elif num1 < num3 < num2:
    print("Aqui estão os valores em ordem decrescente:")
    print(num2, num3, num1)

elif num2 < num1 < num3:
    print("Aqui estão os valores em ordem decrescente:")
    print(num3, num1, num2)

elif num2 < num3 < num1:
    print("Aqui estão os valores em ordem decrescente:")
    print(num1, num3, num2)

elif num3 < num2 < num1:
    print("Aqui estão os valores em ordem decrescente:")
    print(num1, num2, num3)

elif num3 < num1 < num2:
    print("Aqui estão os valores em ordem decrescente:")
    print(num2,num1, num3)

else:
    print("Existe algum valor repetido, tente de novo")
