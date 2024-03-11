altura = int(input("").strip())
comprimento = int(input("").strip())
largura = int(input("").strip())

areaPiso = largura * comprimento
volumeSala = largura * comprimento * altura
areaParede = 2 * altura * largura + 2 * altura * comprimento

print(f'{areaPiso}')
print(f'{volumeSala}')
print(f'{areaParede}')
