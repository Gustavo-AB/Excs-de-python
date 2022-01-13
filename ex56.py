somaDasIdades = 0
nomeDoMaisVelho = ""
maisVelho = 0
menosDe20 = 0

for contador in range(1, 5):
    print("="*15,f"{contador}° Pessoa", "="*15)
    nome = str(input(f"Nome: "))
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo [M/F]: ")).strip().lower()
    somaDasIdades += idade

    if contador == 1 and sexo == "m":
        nomeDoMaisVelho = nome
        maisVelho = idade

    else:
        if idade > maisVelho and sexo == "m":
            nomeDoMaisVelho = nome
            idadeDoMaisVelho = idade

        if idade < 20 and sexo == "f":
            menosDe20 += 1 

    print(" "*15, "CONCLUIDO")


media = somaDasIdades / 4

print("-"*30)
print(f"A média das idades é de {media} anos!")
print(f"O homem mais velho tem {idadeDoMaisVelho} anos, e se chama {nomeDoMaisVelho}!")
print(f"Ao todo são {menosDe20} mulheres com menos de 20 anos!")
print("-"*30)
