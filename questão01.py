num1= int(input("Digite um valor para A: "))
num2= int(input("Digite um valor para B: "))
num3= int(input("Digite um valor para C: "))

if num1 + num2 < num3:
    print("Os valores de A+B:", num1+num2,", são menores do que C: " , num3)
elif num1+num2 == num3:
    print("Os valores de A+B:", num1+num2, ", são iguais a C:", num3)
else:
    print("Os valores de A+B", num1+num2, ", são maiores do que C:", num3)
