# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.


def get_somatorio(num: int) -> int:
    somatorio: int = 0
    for i in range(num + 1):
        somatorio += i
    return somatorio


def main():
    while True:
        try:
            num: int = int(input("Informe um número inteiro: "))
            if num > 0:
                somatorio: int = get_somatorio(num)
                print(f'O somatório de todos os números antes de {num} é:',somatorio)
                break
            else:
                print('O número precisa ser diferente de 0.')
            
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")


if __name__ == "__main__":
    main()
