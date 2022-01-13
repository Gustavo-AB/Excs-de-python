from random import randint

print("Vou pensar em um número de 0 a 5. Tente adivinhar qual número pensei:")

numeroPc = randint(0, 5)
numeroPlayer = int(input("> "))

if numeroPlayer == numeroPc:
    print("Uau! Parabéns você GANHOU!")

else:
    print("Que pena você PERDEU!")

