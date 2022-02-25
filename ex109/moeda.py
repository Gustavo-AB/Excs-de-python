def aumentar(numero=0, porcentagem=0, formatacao=False):
    valor_aumentado = numero + ((numero * porcentagem) / 100)

    return valor_aumentado if not formatacao else moeda(valor_aumentado)


def diminuir(numero=0, porcentagem=0, formatacao=False):
    valor_diminuido = numero - ((numero * porcentagem) / 100)

    return valor_diminuido if not formatacao else moeda(valor_diminuido)


def dobro(numero=0, formatacao=False):
    dobro = numero * 2

    return dobro if not formatacao else moeda(dobro)


def metade(numero=0, formatacao=False):
    metade = numero / 2

    return metade if not formatacao else moeda(metade)


def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')