def voto(nascimento):
    from datetime import date

    idade = date.today().year - nascimento

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
        
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'

    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'


ano_nascimento = int(input("Em que ano voce nasceu? "))
status_de_voto = voto(ano_nascimento)

print(status_de_voto)
