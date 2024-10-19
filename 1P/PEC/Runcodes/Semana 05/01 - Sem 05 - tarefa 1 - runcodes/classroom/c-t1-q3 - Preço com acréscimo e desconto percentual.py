preco = float(input('Qual o preço?: '))
percentual = float(input('Qual o percentual?: '))

def acrecimo(preco, percentual):
    return preco + (preco * percentual / 100)

def desconto(preco, percentual):
    return preco - (preco * percentual / 100)

print(f'O valor com acrécimo é: {acrecimo(preco, percentual):.2f}')
print(f'O valor com acrécimo é: {desconto(preco, percentual):.2f}')

