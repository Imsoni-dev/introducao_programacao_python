'''Escreva um programa que pergunte o pepósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total com juros no período.'''

#pergunta deposito inicial e taxa de juros da poupança
valor_inicial = float(input("Digite o valor inicial da poupança: "))
taxa_juros = float(input("Digite a taxa de juros da poupança: "))

total_com_juros = valor_inicial
meses = 24

print("Mês\tValor com Juros")

for mes in range(1, meses + 1):
    total_com_juros = total_com_juros + total_com_juros * (taxa_juros / 100)
    print(f"{mes}\tR$ {total_com_juros:.2f}")

print("Total com juros: R$ {:.2f}".format(total_com_juros))
