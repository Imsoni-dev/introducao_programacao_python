#programa pagar imposto 
salario = float(input("Digite seu salário atual: "))

if salario > 1200:
    print(f"Você paga imposto, pois recebe {salario:5.2f} de salario")
elif salario == 1200:
    print("Essa foi por pouco, falta um centavo para você pagar impostos")
else:
    print(f"Você ainda não paga imposto pois só recebe {salario:5.2f} de salario")