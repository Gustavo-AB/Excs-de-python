valores = list()

for contador in range (0, 5):
    valores.append(int(input(f"Digite um valor para a posição {contador}: "))) 

maior_valor = max(valores)
menor_valor = min(valores)

print("*"*40)

print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior_valor} na posição ", end="")

for chave, valor in enumerate(valores):
    if valor == maior_valor:
        print(chave, end=" ")

print(f"\nO menor valor digitado foi {menor_valor} na posicao ", end="")

for chave, valor in enumerate(valores):
    if valor == menor_valor:
        print(chave, end=" ")
    