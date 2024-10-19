def identificador(n1):
    resDiv = n1 % 5

    if resDiv == 0:
        return f'O resultado da equação (9n + 7) é: {9 * n1 + 7}'
    elif resDiv == 1:
        return "O número é: par" if n1 % 2 == 0 else "O número é: ímpar"
    elif resDiv == 2:
        return f'O resultado da equação (5n2 – 3n + 42) é: {5 * n1 ** 2 - 3 * n1 + 42}'
    elif resDiv == 3:
        return f'A divisão inteira por 10 é: {n1 // 10}'
    elif resDiv == 4:
        return f"O quadrado do valor é: {n1 ** 2}"

def main():
    n1 = int(input('Insira um número: '))

    print(identificador(n1))

if __name__ == '__main__':
    main()