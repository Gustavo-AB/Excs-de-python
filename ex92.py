from datetime import datetime

cadastro = dict()

cadastro["nome"] = str(input('Digite o nome: '))

ano_nascimento = int(input("Ano de nascimento: "))
cadastro["idade"] = datetime.now().year - ano_nascimento

cadastro["ctps"] = int(input('Carteira de trabalho: (0 caso nao possua)'))

ano_nascimento = 2022 - ano_nascimento

if cadastro["ctps"] != 0:
    cadastro["contratacao"] = int(input("Ano de contratacao: "))
    cadastro["salario"] = float(input("Salario: "))
    cadastro["aposentadoria"] = cadastro["idade"] + ((cadastro["contratacao"] + 35) - datetime.now().year)

print("-"*30)

for chave, valor in cadastro.items():
    print(f' -{chave} tem o valor {valor}!')

