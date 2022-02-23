def leiaInt(msg):
    numero = 0
    
    while True:
        valor = input(msg)

        if valor.isnumeric():
            numero = int(valor)
            break

        else:
            print(f'\033[31mErro! Digite um numero valido\033[m')

    return numero


numero = leiaInt("Digite um numero: ")
print(f'\033[32mVocê digitou o numero {numero}!\033[m')
