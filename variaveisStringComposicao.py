# Juntar várias strings para construir ma mensagem nem sempre é prático. Porém, usando a composição de strigs do Python, é possível escrever de forma simples e clara.
# Marcadores do Tipo:
# Inteiros: %d
# String: %s
# Decimal: %f

nome = 'João'
idade = 36
grana = 15.50
print('%s tem %d anos e R$%f no bolso.' % (nome, idade, grana))
