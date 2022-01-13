sexo = str(input("Digite o seu sexo: ")).strip().lower()[0]

while sexo not in "MmFf":
    sexo = str(input("Dado Inválido\nDigite o seu sexo novamente: ")).strip().lower()

if sexo == "m":
    print("Sexo MASCULINO Registrado!")

else:
    print("Sexo FEMININO Registrado")
