'''programa pergunta velocidade do carro de um usuário
caso ultrapasse 80Km/h, exibe mensagem que ele foi multado. 
exibe o valor da multa que é cobrada por R$5.00 por Km acima de 80Km/h.
'''

velocidade = int(input("Digite em que velocidade estava dirigindo: "))
multa = (velocidade - 80) * 5

if velocidade > 80:
    print("Você dirigiu acima do limite de velocidade por isso foi multado")
    if velocidade > 80:
        print(f"O valor da multa cobrada é: R${velocidade + multa}")

    
