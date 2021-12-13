# Programa que lê dois números e pede ao usuário que escolha uma operação ser realizada.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação: 1 = adição, 2 = subtração, 3 = multiplicação, 4 = divisão: "))
if operacao == 1:
    print(f"O resultado da operação escolhida é: {num1 + num2}")
elif operacao == 2:
    print(f"O resultado da operação escolhida é: {num1 - num2}")
elif operacao == 3:
    print(f"O resultado da operação escolhida é: {num1 * num2}")
elif operacao == 4:
    print(f"O resultado da operação escolhida é: {num1 / num2}")
else:
    print("Desculpe! Você não selecionou uma operação!") # Esta mensagem será exibida ao usuário se este não escolher uma operação!