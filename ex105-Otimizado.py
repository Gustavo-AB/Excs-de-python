def notas(*notas, situacao=False):
    dados_notas = dict()
    dados_notas["quantidade"] = len(notas)
    dados_notas["maior_nota"] = max(notas)
    dados_notas["menor_nota"] = min(notas)
    dados_notas["media"] = (sum(notas)) / len(notas)

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

