# Programa que calcula para o usuário o preço da sua conta de energia elétrica.

kwh = int(input("Digite a quantidade de KWh consumidos: "))
tipo_de_instalacao = str(input("Informe o tipo de Instalção Elétrica: R = (residencial), C = (comercial), I = (industrial): "))
if tipo_de_instalacao == "R" or "r" and kwh <= 500:
    conta = kwh * 0.40
    print(f"O valor da sua fatura de energia é de R${conta:5.2f}")
elif tipo_de_instalacao == "R" or "r" and kwh > 500:
    conta = kwh * 0.65
    print(f"O valor da sua fatura de energia é de R${conta:5.2f}")
elif tipo_de_instalacao == "C" or "c" and kwh <= 1000:
    conta = kwh * 0.55
    print(f"O valor da sua fatura de energia é de R$:{conta:5.2f}")
elif tipo_de_instalacao == "C" or "c" and kwh > 1000:
    conta = kwh * 0.60
    print(f"O valor da sua fatura de energia é de R$:{conta:5.2f}")
elif tipo_de_instalacao == "I" or "i" and kwh <= 5000:
    conta = kwh * 0.55
    print(f"O valor da sua fatura de energia é de R${conta:5.2f}")
elif tipo_de_instalacao == "I" or "i" and kwh > 5000:
    conta = kwh * 0.60
    print(f"O valor da sua fatura de energia é de R${conta:5.2f}")