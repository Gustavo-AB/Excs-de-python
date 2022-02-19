from random import randint
from operator import itemgetter

jogos = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

for chave, valor in jogos.items():
    print(f'{chave}: {valor}')
    
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("-"*40)

for chave, valor in enumerate(ranking):
    print(f'{chave+1}° lugar: {valor[0]} com {valor[1]}')
