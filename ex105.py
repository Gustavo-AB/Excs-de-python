def notas(*notas, situacao=False):
    quantidade = len(notas)
    maior_nota = menor_nota = contador = media = 0
    dados_notas = dict()
    dados_notas["quantidade"] = quantidade

    while contador < quantidade:
        if contador == 0:
            maior_nota = menor_nota = notas[contador]

        else:
            if notas[contador] > maior_nota:
                maior_nota = notas[contador]

            else:
                menor_nota = notas[contador]

        media += notas[contador]
        contador += 1

    
    media /= quantidade
    dados_notas["maior_nota"] = maior_nota
    dados_notas["menor_nota"] = menor_nota
    dados_notas["media"] = media

    if situacao:
        if dados_notas["media"] < 5:
            dados_notas["situacao"] = "Ruim"

        elif dados_notas["media"] < 8:
            dados_notas["situacao"] = "Boa"

        else:
            dados_notas["situacao"] = "Muito boa"

    return dados_notas

n = notas(10,4,8,9, situacao=True)
print(n)
