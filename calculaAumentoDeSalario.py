# Programa que calcula o aumento salarial de um funcionário em 10% caso este receba mais de R$1.250,00 e 15% para quem recebe menos que este valor.

salario = float(input("Digite o valor do seu salário: "))
if salario > 1250:
    novoSalario = salario + (salario * 0.10)
    print(f"Você terá um aumento de 10% no seu salário. E o novo valor será: R${novoSalario:5.2f}")
if salario <= 1250:
    novoSalario = salario + (salario * 0.15)
    print(f"Você terá um aumento de 15% no seu salário. E o novo valor será: R${novoSalario:5.2f}")