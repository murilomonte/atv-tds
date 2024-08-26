def main():
    n = int(input('Insira o valor de N: ').strip())

    if n == 1: n = 2
    h = 1
    indice = 2
    
    while indice <= n:
        h = h + (1/indice)
        indice += 1

    print(f'O valor de H é: {h:.4f}')

if __name__ == '__main__':
    main()