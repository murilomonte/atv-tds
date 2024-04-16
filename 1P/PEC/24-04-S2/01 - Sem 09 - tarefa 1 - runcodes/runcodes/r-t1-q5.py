def identificador(n1):
    resDiv = n1 % 5

    if resDiv == 0:
        return 9 * n1 + 7
    elif resDiv == 1:
        return "par" if n1 % 2 == 0 else "ímpar"
    elif resDiv == 2:
        return 5 * n1 ** 2 - 3 * n1 + 42
    elif resDiv == 3:
        return n1 // 10
    elif resDiv == 4:
        return n1 ** 2

def main():
    n1 = int(input())

    print(identificador(n1))

if __name__ == '__main__':
    main()