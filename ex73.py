times = (
    "Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians", "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos",
    "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá", "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense"
)

print(f"Os 5 Primeiros São: {times[:5]}")
print(f"Os 4 Últimos São: {times[16:]}")
print(f"Os Times em Ordem Alfabética: {sorted(times)}")
print(f"O Time da Chapecoense esta na {times.index('Chapecoense')+1}º Posição!")
