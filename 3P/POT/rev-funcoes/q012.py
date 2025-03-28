# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.


def get_somatorio(num) -> int:
    somatorio: int = 0
    for i in range(num + 1):
        somatorio += i
    return somatorio


def main():
    while True:
        try:
            num: int = int(input('Informe um número inteiro: '))
            somatorio: int = get_somatorio(num)
            print(somatorio)
            break
        except ValueError:
            print('Entrada inválida. Insira um número inteiro.')        

if __name__ == "__main__":
    main()