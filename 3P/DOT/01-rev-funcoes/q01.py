def num_par(num) -> bool:
    if num % 2 == 0:
        return True
    return False

def main():
    while True:
        try:
            num = int(input('Insira um número: '))
            if num_par(num):
                print('É par!')
            else:
                print('É impar!')
                break
        except:
            print('Número inválido. Digite novamente!')

if __name__ == "__main__":
    main()