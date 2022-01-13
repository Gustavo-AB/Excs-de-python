primeiraNota = float(input("Primeira nota: "))
segundaNota = float(input("Segunda notal: "))
media = (primeiraNota + segundaNota) / 2

if media < 5:
    print(f"Com nota {media} o aluno esta REPROVADO!")

elif media < 6.9:
    print(f"Com nota {media} aluno esta de RECUPERAÇÃO!")

else:
    print(f"Com nota {media} o aluno esta APROVADO!")
