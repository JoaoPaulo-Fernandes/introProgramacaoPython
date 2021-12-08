# Programa que calcula o tempo de uma viagem de carro, com base nas informações de velocidade e distância percorrida.
distancia = int(input("Digite a distância a ser percorrida KM: "))
velocidade = float(input("Digite a velocidade média utilizada KM/H: "))
tempo = distancia/ velocidade
print(f"O tempo aproximado da viagem será de: {tempo} horas")