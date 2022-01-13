salarioAtual = float(input("Qual o salario do funcionario? "))
salarioComAumento = salarioAtual + (salarioAtual * 15 / 100)

print(f"O funcionario que ganhava R${salarioAtual:.2f}, com 15% de aumento agora ganha R${salarioComAumento:.2f}!")
