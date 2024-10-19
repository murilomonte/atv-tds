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
    n1 = int(input())
    n2 = int(input())
    opt = int(input())

    calculadora(n1, n2, opt)

if __name__ == '__main__':
    main()