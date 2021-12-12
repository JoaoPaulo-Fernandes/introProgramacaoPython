velocidade = int(input("Digite a velocidade do carro Km/h: "))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f"Você foi multado por excesso de velocidade em R${multa:5.2f}")