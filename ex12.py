precoProduto = float(input("Qual o preco do produto? "))
desconto = precoProduto - (precoProduto * 5 / 100)
print(f"O produto que custava R${precoProduto}, com 5% de desconto agora custa R${desconto:.2f}")
