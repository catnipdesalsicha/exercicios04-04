identificacao= int(input("Digite seu número de identificação: "))
nota1= float(input("Digite a nota da primeira avaliação: "))
nota2= float(input("Digite a nota da segunda avaliação: "))
nota3= float(input("Digite a nota da terceira avaliação: "))
me= float(input("Digite a média dos seus exercícios: "))

MA= (nota1+nota2*2+nota3*3+me)/7

if MA>= 90:
    conceito="A"
elif MA>=75 and MA<90:
    conceito="B"
elif MA>=60 and MA<75:
    conceito="C"
elif MA>=40 and MA<60:
    conceito="D"
else:
    conceito="E"

print("Seu número de identificação é: ", identificacao)
print("Suas notas foram: ", nota1,"/" , nota2,"/", nota3)
print("Sua média de exercícios foi: ", me)
print("Sua média de aproveitamento foi: ", MA)

if conceito == ("A", "B" or "C"):
    print("Aprovado")
else:
    print("Reprovado")