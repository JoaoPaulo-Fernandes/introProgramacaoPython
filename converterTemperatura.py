# Programa que converte a temperatura °C inserida pela usuário para a temperatura °F.
temperatura = int(input("Digite a temperatura a ser convertida °C: "))
f = (9 * temperatura / 5) + 32
print(f"A tempertura informada equivale a {f:2.0f} °F")