'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos
do usuário. Calcule o total em segundos.
'''
d = int(input("Dias: "))
hrs = int(input("Horas: "))
min = int(input("Minutos: "))
seg = int(input("Segundos: "))

print(f"O Total de dias em segundos são {(d * 86400)} segundos")
print(f"O Total de horas em segundos são {(hrs * 3600)} segundos")
print(f"O Total de Minutos em segundos são {(min * 60)} segundos")
print(f"Segundos em Segundos é igual a {seg} segundos")

