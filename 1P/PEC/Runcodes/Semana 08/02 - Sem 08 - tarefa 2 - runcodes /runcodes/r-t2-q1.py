def ePar(n1):
    if (n1 % 2) == 0:
        return n1 + 5
    else:
        return n1 + 8

def main():
    n1 = int(input())

    print(ePar(n1))

if __name__ == '__main__':
    main()