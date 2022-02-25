def aumentar(numero, porcentagem):
    valor_aumentado = numero + ((numero * porcentagem) / 100)

    return f'O valor R${numero} aumentando {porcentagem}% temos R${valor_aumentado}'

def diminuir(numero, porcentagem):
    valor_aumentado = numero - ((numero * porcentagem) / 100)

    return f'O valor R${numero} diminuido em {porcentagem}% temos R${valor_aumentado}'

def dobro(numero):
    dobro = numero * 2

    return f'O dobro de {numero} é {dobro}'

def metade(numero):
    metade = numero / 2

    return f'A metade de {numero} é {metade}'