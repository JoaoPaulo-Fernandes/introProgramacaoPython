# O fatiamento é muito poderoso no Python, funciona com a utilização de dois pontos [:]. Veja os exemplos a seguir!

z = 'abcdef'
print(z[0:2]) # Imprime o resultado do intervalo de 0 até o 2, porém este será excluído da impressão - Dizemos que o final da fatia não é incluído nela. 
              # Sendo impresso apenas as letras (ab)

print(z[0:-1]) # Imprime o resultado do intervalo entre 0 e -1. Observação o -1 indica o sentido da direita para a esquerda. (equilave a letra (f)).