import moeda

valor = int(input("Digite um preco: "))

print(f'O valor {moeda.moeda(valor)} aumentado em 23% é igual a {moeda.moeda(moeda.aumentar(valor, 23))}')
print(f'O valor {moeda.moeda(valor)} diminuido em 23% é igual a {moeda.moeda(moeda.diminuir(valor, 23))}')
print(f'O dobro de {moeda.moeda(valor)} é igual a {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)}  é igual a {moeda.moeda(moeda.metade(valor))}')
