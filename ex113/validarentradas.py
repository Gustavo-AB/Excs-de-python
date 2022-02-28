def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))

        except (ValueError, TypeError):
            print(f'\033[31mErro! Digite um numero INTEIRO valido\033[m')
            continue

        except (KeyboardInterrupt):
            print(f'\033[34m\nEntrada de dados interrompida pelo usuario\033[m')
            return 0

        else:
            return numero


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))

        except (ValueError, TypeError):
            print(f'\033[31mErro! Digite um numero REAl válido\033[m')
            continue
        
        except (KeyboardInterrupt):
            print(f'\033[34m\nEntrada de dados interrompida pelo usuario\033[m')
            return 0

        else:
            return f'{numero}'.replace('.', ',')