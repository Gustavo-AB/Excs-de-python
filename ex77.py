palavras = ("oi", "aprendizado", "python", "programacao", "computador")
vogais = "aeiou"

for palavra in palavras:
    print(f"A palavra {palavra.upper()} Tem as Vogais", end=" ")

    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")
    print("\n", "-"*30)
    