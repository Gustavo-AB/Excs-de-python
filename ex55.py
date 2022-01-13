maiorPeso = 0
menorPeso = 0

for contador in range(1, 6):
    peso = float(input(f"Digite o peso da {contador} pessoa: "))

    if contador == 1:
        maiorPeso = peso
        menorPeso = peso

    else:
        if peso > maiorPeso:
            maiorPeso = peso

        if peso < menorPeso:
            menorPeso = peso

print("="*30)

print(f"O MAIOR peso lido foi de {maiorPeso:.2f}Kg")
print(f"O MENOR peso lido foi de {menorPeso:.2f}Kg")

print("="*30)
