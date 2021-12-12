# Programa que calcula quanto que o usuário deve pagar pela locação de um veículo, com base nos dias e km rodados.
km = int(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade de dias que o carro ficou alugado: "))
preco = km * 0.15 + dias * 60
print(f"O valor a ser pago é de R${preco:5.2f}")