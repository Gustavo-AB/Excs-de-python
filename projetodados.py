import random
from time import sleep
from sys import stdout

cont = 0


numeroDado = input("Aperte enter para lancar o dado! ")
numeroDado = random.randint(1, 6)

while cont < 3 :
    print(".")
    sleep(1)
    cont += 1


print(numeroDado)
