def main():
    num = int(input().strip())
    numAnterior = num 
    while numAnterior != 1:
        if num == 0:
            num = 1
            break
        numAnterior -= 1
        num *= numAnterior
    print(num)

if __name__ == '__main__':
    main()