def valMedia(n1, n2, n3, n4, n5):
    media  = (n1 + n2 + n3 + n4 + n5) / 5
    print(media)
    if n1 > media:
        print(f'{n1:.2f}')
    if n2 > media:
        print(f'{n2:.2f}')
    if n3 > media:
        print(f'{n3:.2f}')
    if n4 > media:
        print(f'{n4:.2f}')
    if n5 > media:
        print(f'{n5:.2f}')

def main():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))
    n4 = int(input('Insira o quarto número: '))
    n5 = int(input('Insira o quinto número: '))

    valMedia(n1, n2, n3, n4, n5)

if __name__ == '__main__':
    main()