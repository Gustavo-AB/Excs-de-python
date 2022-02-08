pessoas = list()
pessoas_pesadas = list()
maior_peso = 0
menor_peso = 0
pessoas_leves = list()
pessoa = list()
contador = 0

while True:
    pessoa.append(str(input("Digite o nome: ")))
    pessoa.append(float(input("Digite o peso: ")))
    pessoas.append(pessoa[:])
    contador += 1
    pessoa.clear()
    continuar_ou_nao = str(input("Deseja continuar [S/N]? "))

    if continuar_ou_nao in "Nn":
        break

print(f"Ao todo foram {contador} pessoas cadastradas!")

for individuo in pessoas:
    if individuo[1] > 80:
        pessoas_pesadas.append(individuo[0])
        maior_peso = individuo[1]

    else:
        pessoas_leves.append(individuo[0])
        menor_peso = individuo[1]

print(f"O maior peso da lista é {maior_peso}Kg. Peso de {pessoas_pesadas}")
print(f"O menor peso da lista é {menor_peso}Kg. Peso de {pessoas_leves}")
