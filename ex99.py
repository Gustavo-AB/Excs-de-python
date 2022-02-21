def maior(* numeros):
    maior = contador = 0

    print("-="*30)
    print("Analisando os numeros...")

    while contador < len(numeros):
        print(numeros[contador], end=" ")
        
        if contador == 0:
            maior = numeros[contador]
        
        else:
            if numeros[contador] > maior:
                maior = numeros[contador]

        contador += 1

    print(f'|=> São {len(numeros)} valores no total!')
    print(f'O maior valor informado foi {maior}')


maior(1, 2, 3,  5)
maior(42,7,2,8,21)

