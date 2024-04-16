def diferenca(n1, n2, n3):
    dif1 = abs(n2 - n1)
    dif2 = abs(n3 - n1)

    if dif1 < dif2:
        return dif1
    else:
        return dif2

def main():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    print(diferenca(n1, n2, n3))

if __name__ == '__main__':
    main()