from random import randint

numeroDoPc = randint(0, 10)
contador = 0

print("\033[37;42m=\033[m"*40,"\n")
print(" "*9,"\033[35mJOGO DA ADIVINHAÇÃO!\n")
print("\033[37;42m=\033[m"*40, "\n")

print("Olá! Eu sou o seu Computador")
print("Acabei de pensar em um número entre 0 e 10!")

palpite = int(input("Tente adivinhar: "))

while palpite != numeroDoPc:
    print("-"*40)
    if palpite < numeroDoPc:
        palpite = int(input("Pensei em um numero \033[35mMAIOR\033[m\nTente novamente: "))

    if palpite > numeroDoPc:
        palpite = int(input("Pensei em um numero \033[35mMENOR\033[m\nTente novamente: "))

    contador += 1

print(f"\033[32mParabens você acertou com {contador} tentativas!\033[m")
print("-"*40)
