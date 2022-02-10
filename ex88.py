from random import randint
from time import sleep

contador = 0
controlador = 1
jogos = []
lista = []

quantidade_palpites = int(input("Quantos jogos você deseja sortear? "))

while controlador <= quantidade_palpites:
    contador = 0
    while True:
        numero = randint(1, 60) 

        if numero not in lista:
            lista.append(numero)
            contador += 1

        if contador >= 6:
            break
    
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

    controlador += 1

for chave, jogo in enumerate(jogos):
    print(f"Jogo {chave+1}: {jogo}")
    contador += 1
    sleep(0.5)

print("Boa sorte!")
