preco = float(input('').strip())
percentual = float(input('').strip())

def acrecimo(preco, percentual):
    return preco + (preco * percentual / 100)

def desconto(preco, percentual):
    return preco - (preco * percentual / 100)

print(f'{acrecimo(preco, percentual):.2f}')
print(f'{desconto(preco, percentual):.2f}')
