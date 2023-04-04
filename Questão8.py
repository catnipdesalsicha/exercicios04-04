peso= float(input("Digite seu peso: "))
altura= float(input("Digite sua altura: "))
imc= peso/(altura)**2

if imc<18.5:
    condicao= "Você está abaixo do peso adequado"
    print("Seu IMC é: ", imc, condicao)
elif imc<25:
    condicao= "Peso normal"
    print("Seu IMC é: ", imc, condicao)
elif imc<30:
    condicao= "Você está acima do peso adequado"
    print("Seu IMC é: ", imc, condicao)
else:
    condicao= "Obeso"
    print("Seu IMC é: ", imc, condicao)
