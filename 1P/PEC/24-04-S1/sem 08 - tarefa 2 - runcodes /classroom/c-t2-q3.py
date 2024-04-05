def buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FIZZBUZZ')
    elif num % 3 == 0:
        print('FIZZ')
    elif num % 5 == 0:
        print('BUZZ')

def main():
    num = int(input('Insira um número: '))
    buzz(num)
if __name__ == '__main__':
    main()