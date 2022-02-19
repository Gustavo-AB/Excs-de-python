jogador = dict()
gols = list()
total = 0

jogador["nome"] = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas foram jogadas? "))

for partida in range(1, partidas+1):
    gols.append(int(input(f"    Quantos gols na {partida}? ")))
jogador["gols"] = gols

for gol in gols:
    total += gol
jogador["total"] = total

print("-=" * 15)
print(jogador)

print("-=" * 15)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}!')

print("-=" * 15)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas!')

for chave, valor in enumerate(jogador["gols"]):
    print(f'    => Na partida {chave+1}, fez {valor} gols!')
print(f'Foi um total de {jogador["total"]}!')
