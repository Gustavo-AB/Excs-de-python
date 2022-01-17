numero = int(input("Digite um numero para saber o seu fatorial: "))
fatorial = 1

while numero > 0:
    if numero == 1:
        print(f"1 =", end=" ")

    else:
        print(f"{numero} X", end=" ")
    fatorial *= numero
    numero -= 1

print(fatorial)

#Com for, e outra forma de realizar uma condicao

numero2 = int(input("Digite um numero para saber o seu fatorial: "))
fatorial2 = 1

for contador in range(1, numero2+1):
    print(f"{numero2} x" if numero2 > 1 else f"= {fatorial2}", end=" ")
    fatorial2 *= numero2
    numero2 -= 1
