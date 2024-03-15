numero = int(input('Informe um número entre 1000 e 9999: '))

def numReverso(numero):
    d1 = numero // 1000
    d2 = (numero % 1000) // 100
    d3 = (numero % 100) // 10
    d4 = (numero % 10) // 1
    return (d4 * 1000) + (d3 * 100) + (d2 * 10) + (d1 * 1)

print(f'O reverso desse número é: {numReverso(numero)}')