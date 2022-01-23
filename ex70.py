total = mais_de_mil = contador = 0
nome_mais_barato = ""
mais_barato = 0

while True:
    nome_produto = str(input("Digite o nome do produto: ")).strip().lower()
    preco = int(input("Digite o preco do produto: "))

    total += preco
    contador += 1

    if preco > 1000:
        mais_de_mil += 1

    if contador == 1:
        nome_mais_barato = nome_produto
        mais_barato = preco

    else:
        if preco < mais_barato:
            mais_barato = preco

    continuar_ou_nao = str(input("Deseja continuar? [S/N]")).strip().lower()

    if continuar_ou_nao in "Nn":
        break

print(f"O total da compra é de R${total}!")
print(f"{mais_de_mil} produto(s) custam mais de mil reais!")
print(f"O menor preco foi de R${mais_barato}")
