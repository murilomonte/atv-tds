valor = float(input('Insira o valor do produto: '))

desconto = valor * 0.10
valorFinal = valor - desconto

print(f'Com o desconto de 10% o valor final é {valorFinal:.2f}')