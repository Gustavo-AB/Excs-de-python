matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha = coluna = soma_dos_pares = soma_da_linha3 = maior_da_linha2 = contador = 0

while True:
    matriz[linha][coluna] = int(input(f"Digite o numero [{linha}, {coluna}]: "))
    coluna += 1

    if coluna == 3:
        coluna = 0
        linha += 1

    if linha == 3:
        break

for l in range(0, 3):
    for c in range(0, 3):
        print(f"|{matriz[l][c]:^5}", end="|")
    print()

for linha in matriz:
    for chave, valor in enumerate(linha):
        if valor % 2 == 0:
            soma_dos_pares += valor

        if contador == 1:
            if valor > maior_da_linha2:
                maior_da_linha2 = valor

        if contador == 2:
            soma_da_linha3 += valor
    contador += 1

print(f"A soma dos numeros pares é igual a {soma_dos_pares}!")
print(f"A soma dos numeros da linha 3 é igual a {soma_da_linha3}")
print(f"O maior valor da linha 2 é o {maior_da_linha2}!")
