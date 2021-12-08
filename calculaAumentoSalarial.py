# Programa que calcula o aumento salarial do usuário com base nos dados informados por este. Em seguida, exibe o valor da porcentagem do aumento e do novo salário.
salario = float(input("Digite o valor do seu salário: "))
porcentagem_aumento = int(input("Digite o valor da porcentagem do aumento salarial: "))
novo_salario = salario + (salario * porcentagem_aumento)/100
print(f"O seu novo salário será de: R$ {novo_salario:5.2f}")
