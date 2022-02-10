nota = []
ficha = []
fichas = []
media_individual = 0

while True:
    contador = 1

    nome = str(input("Nome: "))
    ficha.append(nome)
    nota.append(float(input(f"Nota {contador}: ")))
    contador += 1
    nota.append(float(input(f"Nota {contador}: ")))
    ficha.append(nota[:])

    media_individual = (nota[0] + nota[1]) / 2
    ficha.append(media_individual)
    fichas.append(ficha[:])

    nota.clear()
    ficha.clear()

    continuar_ou_nao = str(input("Deseja continuar [S/N]? "))

    if continuar_ou_nao in "Nn":
        break

print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print("-"*26)

for chave, valor in enumerate(fichas):
    print(f"{chave:<4}{valor[0]:<10}{valor[2]:>8.1f}")

print("-"*26)

while True:
    mostrar_notas = int(input("Deseja mostrar as notas de qual aluno? (999 interrompe): "))

    if mostrar_notas == 999:
        break

    print(f"Notas de {fichas[mostrar_notas][0]}: {fichas[mostrar_notas][1]}")
    print("-"*26)

print("-"*26)
print("Programa encerrado! ")
