import moeda

valor = int(input("Digite um preco: "))

print(f'O valor {moeda.moeda(valor)} aumentado em 23% é igual a {moeda.aumentar(valor, 23, True)}')
print(f'O valor {moeda.moeda(valor)} diminuido em 23% é igual a {moeda.diminuir(valor, 23, True)}')
print(f'O dobro de {moeda.moeda(valor)} é igual a {moeda.dobro(valor, True)}')
print(f'A metade de {moeda.moeda(valor)}  é igual a {moeda.metade(valor, True)}')