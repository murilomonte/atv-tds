def quaOuRet(base, altura):
    if base == altura:
        return "QUADRADO"
    else:
        return f'{(altura * 2) + (base * 2)} - {altura * base}'

def main():
    base = int(input())
    altura = int(input())

    print(quaOuRet(base, altura))

if __name__ == '__main__':
    main()
