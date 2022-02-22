def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome}, marcou {gols} gols')


nome = str(input("Digite o nome do Jogador: ")).strip()
gols = input("Digite o numero de gols: ")

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome == '':
    ficha(gols=gols)

else:
    ficha(nome, gols)

print("-"*30)
