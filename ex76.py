print("-"*35)
print(f'{"Listagem de Preço":^35}')
print("-"*35)

produtos = (
    "Caderno", 7.80, 
    "Lápis", 1.25, 
    "Borracha", 3, 
    "Mochila", 30, 
    "Estojo", 5
)

for produto in produtos:
    if type(produto) is str:
        print(f"{produto} ", end="."*(26-len(produto)))

    if type(produto) is int or type(produto) is float:
        print(f" R${produto:>5.2f}", end=" ")
        print("\n")
    
