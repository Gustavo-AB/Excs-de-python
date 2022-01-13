diasAlugados = int(input("Por quantos dias o veiculo foi alugado? "))
kmPercorridos = float(input("Quantos km foram percorridos com o veiculo? "))

custoPorKmRodado = kmPercorridos * 0.15
custoPorDiasAlugados = diasAlugados * 60 
totalPagar = custoPorKmRodado + custoPorDiasAlugados

print(f"O total a pagar é de R${totalPagar:.2f}, por {diasAlugados:.0f} dias alugados e {kmPercorridos:.2f} km rodados!")
