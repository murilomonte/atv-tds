def pesoIdeal(altura, sexo):
    if sexo == 1:
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7

def main():
    altura = float(input())
    sexo = int(input())
    print(f'{pesoIdeal(altura, sexo):.2f}')

if __name__ == '__main__':
    main()