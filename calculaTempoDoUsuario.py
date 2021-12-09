# Programa que calcula o tempo de um usuário, com base nas seguintes informações: Dias, horas, minutos e segundos.

dias = int(input("Digite a quantidade de dias de um usuário: "))
horas = int(input("Digite a quantidade de horas de um usuário: "))
minutos = int(input("Digite a quantidade de minutos de um usuário: "))
segundos = int(input("Digite a quantidade de segundos de um usuário: "))
tempo = dias * 86400 + horas * 3600 + minutos * 60 + segundos
print(f"A quantidade de tempo do usuário equivale a {tempo} segundos")