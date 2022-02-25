from modulosparaexcs import moeda

valor = int(input("Digite um preco: "))

print(moeda.aumentar(valor, 23))
print(moeda.diminuir(valor, 23))
print(moeda.dobro(valor))
print(moeda.metade(valor))
