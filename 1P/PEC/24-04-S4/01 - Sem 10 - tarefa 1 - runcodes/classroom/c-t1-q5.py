def main ():
    maior = 0
    for i in range(100):
        entrada = int(input('Digite um número: '))
        if entrada > maior:
            maior = entrada

    print('O maior número é:', maior)

if __name__ == "__main__":
    main()