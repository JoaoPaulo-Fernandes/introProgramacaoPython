# Programa que calcula o preço de uma passagem para o usuário, com base nas informações de Km a serem percorridos.

km = int(input("Qual é a distância em Km da sua viagem? "))
if km <= 200:
    preco = km * 0.50
    print(f"O preço da sua passagem é de R${preco:5.2f}")
if km > 200:
    preco = km * 0.45
    print(f"O preço da sua passagem é de R${preco:5.2f}") 
