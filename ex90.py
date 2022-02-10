aluno = {}

aluno["nome"] = str(input('Nome do aluno(a): '))
aluno["media"] = float(input(f'Média de {aluno["nome"]}: '))

if aluno["media"] >= 6.5:
    aluno["situacao"] = "Aprovado(a)!"

else:
    aluno["situacao"] = "Reprovado(a)!"

print(f'O nome do aluno(a) é igual a {aluno["nome"]}!')
print(f'A média é igual a {aluno["media"]}!')
print(f'A situacao é igual a {aluno["situacao"]}')
