import typing


texto = input("Digite algo: ")

print(f"O tipo primitivo é {type(texto)}")
print(f"Só tem espacos {texto.isspace()}")
print(f"É um numero? {texto.isnumeric()}")
print(f"É alfanumerico? {texto.isalnum()}")
print(f"Esta em maiuscula? {texto.isupper()}")
print(f"Esta em minuscula? {texto.islower()}")
print(f"Esta capitalizado? {texto.istitle()}")
