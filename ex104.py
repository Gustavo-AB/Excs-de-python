def leiaInt(msg):
    numero = 0
    
    while True:
        valor = input(msg)

        if valor.isnumeric():
            numero = int(valor)
            break

        else:
            print(f'Erro! Digite um numero valido')

    return numero


numero = leiaInt("Digite um numero: ")
print(f'Você digitou o numero {numero}!')

