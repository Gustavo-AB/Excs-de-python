larguraParede = float(input("Largura da parede: "))
alturaParede = float(input("Largura da parede: "))
area =  larguraParede * alturaParede
litrosDeTinta = area / 2

print(f"Sua parede tem a dimensão de {larguraParede}x{alturaParede}, e sua area é de {area}m")
print(f"Para pintar essa parede você precisara de {litrosDeTinta}L de tinta!")
