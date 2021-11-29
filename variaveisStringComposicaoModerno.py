# Juntar várias strings para construir ma mensagem nem sempre é prático. Porém, usando a composição de strigs do Python, é possível escrever de forma simples e clara.
# Marcadores do Tipo:
# Inteiros: %d
# String: %s
# Decimal: %f

# nome = 'João'
# idade = 36
# grana = 15.50
# print('%s tem %d anos e R$%f no bolso.' % (nome, idade, grana))

# Esta forma substituída nas versões mais modernas do Python pelo (format): Veja o exemplo abaixo, utilizando o mesmo código acima.

nome = 'João'
idade = 36
grana = 15.50
print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))

