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


def resumo(valor, aumento, reducao):
    print(f'~'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print(f'~'*40)

    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de reducao: \t{diminuir(valor, reducao, True)}')

    print(f'~'*40)
    