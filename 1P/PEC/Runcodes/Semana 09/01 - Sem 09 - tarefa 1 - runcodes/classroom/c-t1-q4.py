def diferenca(n1, n2, n3):
    dif1 = abs(n2 - n1)
    dif2 = abs(n3 - n1)

    if dif1 < dif2:
        return dif1
    else:
        return dif2

def main():
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    n3 = int(input('Insira o terceiro valor: '))

    print(f'A menor diferença é: {diferenca(n1, n2, n3)}')

if __name__ == '__main__':
    main()