

numero = int(input("Digite um numero inteiro: "))
multiplicador = 0

for contador in range(1, numero+1):
    if numero % contador == 0:
        multiplicador += 1
        print('\033[32m', end="") 

    else:
        print('\033[31m', end="")

    print(f"{contador}\033[m", end=" ")


if multiplicador == 2:
    print(f"| O numero {numero} é \033[1;32mSIM\033[m um numero PRIMO porque foi divisivel {multiplicador} vezes")

else:
    print(f"| O numero {numero} \033[31mNÃO\033[m é um numero primo porque foi divisivel {multiplicador} vezes")
