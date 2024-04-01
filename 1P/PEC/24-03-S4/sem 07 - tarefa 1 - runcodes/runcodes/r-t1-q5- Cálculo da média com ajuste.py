n1 = float(input('').strip())
n2 = float(input('').strip())
n3 = float(input('').strip())

def calcMedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    if n3 > 8:
        media += 1
        
    if media > 10:
        media = 10

    return media

print(f'{calcMedia(n1, n2, n3):.2f}')
