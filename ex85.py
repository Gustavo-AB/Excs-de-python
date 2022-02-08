numeros = [[], []]

for contador in range(1, 8):
    numero = int(input(f"Digite o {contador}° número: "))

    if numero % 2 == 0:
        numeros[0].append(numero)

    else:
        numeros[1].append(numero)

print(f"Os numeros pares são {sorted(numeros[0])}!")
print(f"Os numeros impares são {sorted(numeros[1])}!")
