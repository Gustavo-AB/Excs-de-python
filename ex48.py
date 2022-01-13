contador = 0
soma = 0

for numero in range(1, 500, 2):
    if numero % 3 == 0:
        contador += 1
        soma += numero

print(f"A soma dos {contador} valores é igual a {soma}!")
