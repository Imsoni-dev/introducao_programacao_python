'''escreva um prograa que imprima da 1 até o número digitado pelo usuário, mas apenas os números 
ímpares.'''

n_final = int(input("Digite o último número: "))
x = 0 
while x <= n_final:
    if x % 2 == 1:
        print(x)
        x += 1