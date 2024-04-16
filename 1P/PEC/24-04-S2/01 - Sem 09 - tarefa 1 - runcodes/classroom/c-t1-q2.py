def calculadora(n1, n2, opt):
    if opt == 1:
        print(f'{n1 + n2:.2f}')
    elif opt == 2:
        print(f'{n1 - n2:.2f}')
    elif opt == 3:
        print(f'{n1 * n2:.2f}')
    elif opt == 4:
        print(f'{n1 / n2:.2f}')
    else:
        print('Digite uma opção válida')
    
def main():
    print('Calculadora\n1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 – Divisão')
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
    opt = int(input('Qual operação?: '))

    calculadora(n1, n2, opt)

if __name__ == '__main__':
    main()