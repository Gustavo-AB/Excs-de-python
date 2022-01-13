from datetime import date

anoAtual = date.today().year
maiorDeIdade = 0
menorDeIdade = 0

for contador in range(1, 8):
    anoNascimento = int(input(f"Digite o ano de nascimento da {contador} pessoa: "))
    idade = anoAtual - anoNascimento
    contador += 1
    if idade >= 18:
        maiorDeIdade += 1

    else:
        menorDeIdade += 1

print(f"Dentre as 7 pessoas {maiorDeIdade} são Maior de Idade\nE {menorDeIdade} são menores de idade")
