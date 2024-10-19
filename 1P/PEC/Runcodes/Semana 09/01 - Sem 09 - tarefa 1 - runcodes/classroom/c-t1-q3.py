def quaOuRet(base, altura):
    if base == altura:
        return "QUADRADO"
    else:
        return f'{(altura * 2) + (base * 2)} - {altura * base}'

def main():
    print('Insira o tamanho: ')
    base = int(input('Base: '))
    altura = int(input('Altura: '))

    print(quaOuRet(base, altura))

if __name__ == '__main__':
    main()
