cadastro = dict()
lista_cadastro =  list()
lista_de_mulheres = list()

media = 0

while True:
    cadastro["nome"] = str(input("Digite o nome: ")).strip()
    cadastro["sexo"] = str(input("Digite o sexo [M/F]: ")).strip().lower()

    while cadastro["sexo"] not in "mMFf":
        cadastro["sexo"] = str(input("\033[31mErro!\033[m Digite apenas \033[32mM\033[m ou \033[32mF\033[m: ")).strip().lower()

    cadastro["idade"] = int(input("Digite a idade: "))

    lista_cadastro.append(cadastro.copy())
    cadastro.clear()

    continuar_ou_nao = str(input("Deseja continuar? [S/N]")).strip().lower()

    while continuar_ou_nao not in "SsNn":
        continuar_ou_nao = str(input("\033[31mErro!\033[m Digite apenas \033[32mS\033[m ou \033[32mN\033[m: ")).strip().lower()

    if continuar_ou_nao in "Nn":
        break

total_cadastro = len(lista_cadastro)

print("-"*50)
print(f'A) Ao todo temos {total_cadastro} pessoas cadastradas.')

for cadastro in lista_cadastro:
    media += cadastro["idade"]
media /= len(lista_cadastro)

print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end="")

for cadastro in lista_cadastro:
    if cadastro["sexo"] in "Ff":
        lista_de_mulheres.append(cadastro["nome"])

for mulher in lista_de_mulheres:
    print(mulher, end=" ")

print()
print(f'D) Lista de pessoas que estao acima da média:')

for cadastro in lista_cadastro:
    if cadastro["idade"] > media:
        print(f'  =>nome = {cadastro["nome"]}; sexo = {cadastro["sexo"]}; idade = {cadastro["idade"]}')

print('<===Encerrado===>')
