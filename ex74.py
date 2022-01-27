from random import randint

numeros = (
    randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),
)

maior_valor = max(numeros)
menor_valor = min(numeros)

for numero in numeros:
    print(numero, end=" ")

print(f"\nO Maior numero da lista é o {maior_valor}")
print(f"O Menor numero da lista é o {menor_valor}")
