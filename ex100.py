from random import randint, shuffle
from time import sleep

def sortear(lista):
    print("Sorteando 5 valores", end=" ")

    for numero in range(0, 5):
        numero = randint(1, 10)
        lista.append(numero)
        print(numero, end=" ", flush=True)
        sleep(0.3)

    print("Pronto!")

def somarPares(lista):
    soma = 0

    for numero in lista:
        if numero % 2 == 0:
            soma += numero

    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()

sortear(numeros)
somarPares(numeros)
