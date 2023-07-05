'''escreva um programa que leia dois números e que pergunte qual operação você deseja
realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) 
e divisão (/). Exiba o resultado da operação solicitada.
''' 
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operação inválida.")
    exit()

print("Resultado:", resultado)