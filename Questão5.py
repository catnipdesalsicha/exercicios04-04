num= int(input("Digite um número: "))
par = num % 2

if par == 0:
    print("Seu número é par, logo:", num,"+ 5 será:", num+5)
else:
    print("Seu número é ímpar, logo:", num, "+ 8 será:", num+8)