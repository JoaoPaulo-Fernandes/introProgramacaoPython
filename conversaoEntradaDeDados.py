# A função (input) sempre retornará um valor do tipo (string), mesmo você digitando número! Para corrigir essa situação
# utilizaremos (int) para converter para um valor inteiro e (float) para converter para um número decimal ou de ponto flutuante.

# Exemplo:
anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bônus de R${bonus:5.2f}")