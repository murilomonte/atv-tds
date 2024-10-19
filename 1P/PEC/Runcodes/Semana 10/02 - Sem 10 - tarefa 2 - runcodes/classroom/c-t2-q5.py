def simulacao(valor):
    for i in range(1, 25):
        div = valor / i
        print(f'{i}x de R$ {div:.2f}')

def main():
    valor = int(input('Insira um valor para simular a quantidade de prestações: '))
    simulacao(valor)

if __name__ == "__main__":
    main()