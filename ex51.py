print("="*30,"\n10 TERMOS DE UMA PA")
print("="*30)

numeroDaPA = int(input("Digite o termo da PA: "))
razaoDaPA = int(input("Digite a razao da PA: "))
decimo = numeroDaPA + (10-1) * razaoDaPA

for controle in range(numeroDaPA, decimo+razaoDaPA, razaoDaPA):
    print(controle, end="-")

print("Acabou!")
