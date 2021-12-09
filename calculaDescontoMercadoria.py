# Programa que solicita do usuário o preço de uma mercadoria, o percentual de desconto. Depois exibe o valor do desconto e o preço a pagar.
preco = float(input("Digite o valor da mercadoria: "))
percentual_desconto = int(input("Digite o valor do percentual de desconto %: "))
novo_preco = preco - (preco * percentual_desconto)/100
print(f"O valor da mercadoria após o desconto é R$: {novo_preco:5.2f}")