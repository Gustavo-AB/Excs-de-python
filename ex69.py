print("\033[32m=\033[m" * 30)
print(" "* 4, "Cadastro de Pessoas!")
print("\033[32m=\033[m" * 30)

maior_de_idade = homem = mulher_menos_de_vinte = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: ")).strip().lower()

    if idade > 18:
        maior_de_idade += 1

    if sexo in "Mm":
        homem += 1

    if sexo in "Ff" and idade < 18:
        mulher_menos_de_vinte += 1

    continuar_ou_nao = str(input("Deseja cadastrar mais alguem [S/N]")).strip().lower()

    if continuar_ou_nao == "n":
        break

    print("-"*30)

print("-"*30)
print(f"Total de pessoas com mais de 18 anos: {maior_de_idade}!")
print(f"Ao todo temos {homem} homem(s) cadastrados!")
print(f"Ao todo temos {mulher_menos_de_vinte} mulher(s) com menos de 20 anos!")
