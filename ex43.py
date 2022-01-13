peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu imc é de {imc:.2f}, você esta ABAIXO do peso!")

elif imc <= 25:
    print(f"Seu imc é de {imc:.2f}, você esta no pedo IDEAL!")

elif imc <= 30:
    print(f"Seu imc é de {imc:.2f}, você esta com SOBREPESO!") 

elif imc <= 40:
    print(f"Seu imc é de {imc:.2f}, voce esta com OBESIDADE!")

else: 
    print(f"Seu imc é de {imc:.2f}, você esta com OBESIDADE MORBIDA!")
    
