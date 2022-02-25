def aumentar(numero=0, porcentagem=0):
    valor_aumentado = numero + ((numero * porcentagem) / 100)

    return valor_aumentado

def diminuir(numero=0, porcentagem=0):
    valor_diminuido = numero - ((numero * porcentagem) / 100)

    return valor_diminuido

def dobro(numero=0):
    dobro = numero * 2

    return dobro

def metade(numero=0):
    metade = numero / 2

    return metade

def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')