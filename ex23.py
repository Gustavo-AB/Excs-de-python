numero = int(input("Informe um valor: "))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f"{unidade} Unidade\n{dezena} Dezena\n{centena} Centena\n{milhar} Milhar!")
