valores = list()

for contador in range (0, 5):
    numero = int(input("Digite um valor: "))

    if contador == 0 or numero > valores[-1]:
        print(f"Numero {numero} adicionado no final da lista!")
        valores.append(numero)

    else:
        posicao = 0
        print(posicao)

        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print(f"Numero {numero} adicionado na posicao {posicao} da lista!")
                break

            posicao += 1

print(valores)
