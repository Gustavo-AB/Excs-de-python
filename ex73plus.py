times = (
    "zero", "Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos",
    "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense"
    )

print("-="*40)

while True:
    print("Os 5 Primeiros São:")

    for posicao, time in enumerate(times):
        if posicao > 0 and posicao < 5:
            print(f"{posicao}º {time} ", end="| ")

        if posicao == 5:
            print(f"{posicao}º {time}")
            break
    
    print("-"*60)

    print("Os 4 Ultimos São:")

    for posicao, time in enumerate(times):
        if posicao > 16:
            print(f"{posicao}º {time} ", end="| ")

    print("\n","-"*60)

    print("Os Times em Ordem Alfabética:")    

    for posicao, time in enumerate(times):
        if posicao > 0:
            print(sorted(times))
            break
    
    print("-"*60)

    print("O Time da Chapecoense esta na {}º Posição!".format(times.index("Chapecoense")))

    print("-"*60)

    break

print("Fim")
print("-="*40)
