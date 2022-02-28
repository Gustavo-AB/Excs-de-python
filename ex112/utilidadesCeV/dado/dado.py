def leiaDinheiro(msg):
    numero = 0

    while True:
        valor = str(input(msg)).replace(',', '.').strip()

        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO! \"{valor}\" não é um valor válido!\033[m')


        else:
            numero = float(valor)
            break
    
    return numero

