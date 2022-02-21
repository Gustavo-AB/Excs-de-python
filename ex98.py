from time import sleep

def divisor(qnt=30):
    print("-="*qnt)

def contador(inicio=1, fim=10, passo=1):
    divisor()

    print("Contagem de 1 até 10 de 1 em 1: ")

    for numero in range(inicio, fim+1, passo):
        print(numero, end=" ", flush=True)
        sleep(0.5)
    print("Fim!")

    divisor()
  
    print("Contagem de 10 até 0 de 2 em 2:")

    for numero in range(fim, inicio, -2):
        print(numero, end=" ", flush=True)
        sleep(0.5)
    print("Fim!")

    divisor()

    print("Agora é a sua vez de personalizar a contagem! ")
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}:')

    if inicio > fim:
        for numero in range(inicio, fim-1, -passo):
            print(numero, end=" ", flush=True)
            sleep(0.5)
        print("Fim!")

    else:
        for numero in range(inicio, fim+1, passo):
            print(numero, end=" ", flush=True)
            sleep(0.5)
        print("Fim!")

contador()

