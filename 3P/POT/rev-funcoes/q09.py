# 9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos
# no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.


def get_num() -> int:
    while True:
        try:
            num: int = int(input("> "))
            return num
        except ValueError:
            print("Entrada inválida. Insira um número: ")


def get_soma(n1, n2) -> int:
    soma: int = 0
    for i in range(n1, n2 + 1):
        if i == n1:
            soma = i
        else:
            soma += i
    return soma


def main():
    print("Insira o primeiro número: ")
    n1: int = get_num()

    print("Insira o segundo número: ")
    n2: int = get_num()

    soma = get_soma(n1, n2)
    print(f"A soma de todos os números entre {n1} -> {n2} = {soma}")


if __name__ == "__main__":
    main()
