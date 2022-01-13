salario = float(input("Digite o salario do funcionario: "))

if salario > 1250:
    aumentoSalario = salario + (salario * 10 / 100)

else:
    aumentoSalario = salario + (salario * 15 / 100)

print(f"Apartir de agora o funcionario recebe R${aumentoSalario:.2f} de salario")
