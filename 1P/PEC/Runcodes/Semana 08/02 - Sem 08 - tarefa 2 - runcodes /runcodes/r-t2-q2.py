def separaNum(num):
    if 0 < num < 100000:

        u = num % 10 
        num = num // 10

        d = num % 10
        num = num //  10
        
        c = num % 10
        num = num //  10

        uM = num % 10
        num = num  // 10

        dM = num % 10
        num = num  // 10

        cM = num % 10
        num = num  // 10
    else:
        return -1
    
    return u + d + c + uM + dM + cM

def main():
    num = int(input(''))
    print(separaNum(num))

if __name__ == '__main__':
    main()