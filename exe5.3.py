'''faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
o programa deve imprimir 10, 9, 8,...,1, 0 e fogo! na tela. '''

x = 10
while x >= 0:
    print(x)
    x -= 1
    if x < 0:
        print("FOGO!")