valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o seu salario? "))
anosParaFinanciar = int(input("Em quantos anos você deseja financiar a casa? "))

prestacao = valorCasa / (anosParaFinanciar * 12)
taxaDeAprovacao = salario * 30 /100

print(f"Para pagar uma casa de R${valorCasa:.2f} em {anosParaFinanciar} anos as prestações serão de R${prestacao:.2f}")

if prestacao >= taxaDeAprovacao:
    print("Emprestimo NEGADO!")

else:
    print("Emprestimo APROVADO!")
