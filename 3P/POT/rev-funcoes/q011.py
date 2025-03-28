# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.


def get_divisores(num) -> list[int]:
    divisores: list[int] = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores


def main() -> None:
    while True:
        try:
            num: int = int(input("Insira um número inteiro positivo: "))
            divirores: list[int] = get_divisores(num)
            print('Os divisores desse valor são:', divirores)
            break
        except ValueError:
            print("Entrada inválida. Digite um número.")


if __name__ == "__main__":
    main()
