preco = float(input('Insira o primeiro valor: '))

print(f'Pagamento a vista: {preco - (preco * (9/100)):.2f}')
print(f'Pagamento em 5x: {preco / 5:.2f}')
print(f'Pagamento em 10x {(preco + (preco * (17/100))) / 10:.2f}')