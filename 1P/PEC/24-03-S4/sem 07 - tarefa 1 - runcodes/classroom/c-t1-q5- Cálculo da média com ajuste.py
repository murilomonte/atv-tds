n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))

def calcMedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    if n3 > 8:
        media += 1
        
    if media > 10:
        media = 10

    return media

print(f'A média é: {calcMedia(n1, n2, n3):.2f}')
