matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha = 0
coluna = 0

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
