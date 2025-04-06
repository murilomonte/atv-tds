# 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)


def calc(n: int) -> float:
    res: float = 0
    for i in range(1, n + 1):
        res += ((i**2) + 1) / (i + 3)
    return res


def main():
    while True:
        try:
            num: int = int(input("Insira um número inteiro positivo: "))
            res: float = calc(num)
            if num > 0:
                print(
                    f"O resultado da equação: S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(N^2+1)/(N+3). Sendo N = {num} é igual a: {res:.2f}"
                )
                break
            else:
                print('O número precisa ser diferente de 0.')
        except ValueError:
            print("Entrada inválida.")


if __name__ == "__main__":
    main()
