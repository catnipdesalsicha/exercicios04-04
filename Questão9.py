preco= float(input("Digite o preço de etiqueta do produto: "))
print("Condições de pagamento: "
      "1. Á vista (dinheiro ou cheque)  "
      "2.Á vista (crédito)  "
      "3.Parcelado 2X")
condicao= int(input("Digite a que você deseja (1, 2 ou 3):"))

if condicao ==1:
      total= preco*0.9
      print("Seu valor total será: ", total)
elif condicao ==2:
      total= preco*0.85
      print("Seu valor total será: ", total)
elif condicao ==3:
      total= preco
      print("Seu valor total será: ", total, "sem juros")
else:
      print("Você digitou uma condição de pagamento inválida, tente novamente")