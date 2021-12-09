# Programa que ler três números informados pelo usuário, depois imprime o maior e o menor.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
print("====================================================")
if num1 > num2 and num1 > num3:  # Compara se o primeiro número é maior que o segundo e terceiro número
    print(f"O primeiro número é o maior de todos: {num1}")
if num2 > num3 and num2 > num1: # Compara se o segundo número é maior que o terceiro e primeiro número
    print(f"O segundo número é o maior de todos: {num2}")
if num3 > num2 and num3 > num1: # Compara se o terceiro número é maior que o primeiro e segundo número
    print(f"O terceiro número é o maior de todos: {num3}")

if num1 < num2 and num1 < num3: # Compara se o primeiro número é menor que o segundo e terceiro número
    print(f"O primeiro número é o menor de todos: {num1}")
if num2 < num1 and num2 < num3: # Compara se o segundo número é menor que o terceiro e primeiro número
    print(f"O segundo número é o menor de todos: {num2}")
if num3 < num2 and num3 < num1: # Compara se o terceiro número é menor que o primeiro e segundo número
    print(f"O terceiro número é o menor de todos: {num3}")