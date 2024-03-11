altura = int(input("Altura: "))
comprimento = int(input("Comprimento: "))
largura = int(input("Largura: "))

areaPiso = largura * comprimento
volumeSala = largura * comprimento * altura
areaParede = 2 * altura * largura + 2 * altura * comprimento

print(f'A área do piso da sala é: {areaPiso}')
print(f'O volume da sala é: {volumeSala}')
print(f'A área das paredes da sala: {areaParede}')
