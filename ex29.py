velo = float(input("Qual a velocidade do carro? Km"))

if velo <= 80:
    print("Tenha um bom dia e dirija com segurança!")

else: 
    limite = (velo - 80) * 7
    print(f"Você ultrapassou o limite de velocidade e devera pagar uma multa de R${limite:.2f}")
