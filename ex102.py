def fatorial(numero, show=False):
    calculo_fatorial = 1

    if show:
        for contador in range(numero, 0, -1):
            calculo_fatorial *= contador
            print(f'{calculo_fatorial}x{contador}', end=" ")

    else:
        for contador in range(numero, 0, -1):
            calculo_fatorial *= contador

        print(f'O fatorial de {numero}', end=" ")

    print('=', end=" ")
    return calculo_fatorial

print("-"*30)
print(fatorial(5, True))
