jogador = dict()
jogadores = list()
gols = list()

while True:
    total = 0
    jogador["nome"] = str(input("Nome do jogador: "))
    partidas = int(input("Quantas partidas foram jogadas? "))

    for partida in range(1, partidas+1):
        gols.append(int(input(f"    Quantos gols na {partida}? ")))
    jogador["gols"] = gols[:]

    for gol in gols:
        total += gol
    jogador["total"] = total


    continuar_ou_nao = str(input("Deseja continuar? [S/N]")).strip().lower()

    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()


    if continuar_ou_nao in "Nn":
        break

print("=-"*25)
print(f'{"cod":<6}{"nome":<15}{"gols":<10}{"total":>10}')
print("-"*50)

indice = 0

for jogador_time in jogadores:
    print(f'{indice:<6}{jogador_time["nome"]:<15}{jogador_time["gols"]}{jogador_time["total"]:>10}')

    indice += 1
    
print("-"*50)

while True:
    levantamento = int(input("Deseja mostras os dados de qual jogador? (999 para encerrar)"))

    if levantamento == 999:
        break

    else:
        indice2 = 0

        print(f'  --Levantamento de dados do jogador {jogadores[levantamento]["nome"]}')

        for indice in range(1, len(jogadores[levantamento]["gols"])+1):
            print(f'     =>No jogo {indice} marcou {jogadores[levantamento]["gols"][indice2]}')

            indice2 += 1

        print("-"*50)

print("===>ENCERRADO<===")
