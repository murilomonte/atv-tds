# 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + ½! + 1/3! + 1 /N!


def calc(n: int) -> float:
    res: float = 0
    for i in range(1, n + 1):
        res += 1 / fatorial(i)
    return res


def fatorial(num: int) -> float:
    res: float = 1
    for i in range(1, num + 1):
        res *= i
    return res

def main():
    while True:
        try:
            num: int = int(input("Insira um número inteiro positivo: "))
            res: float = calc(num)
            if num > 0:
                print(
                    f"O resultado da equação: S = 1 + 1/1! + 1/N! + 1/3! + 1 /N!. Sendo N = {num} é igual a: {res:.2f}"
                )
                break
            else:
                print('O número precisa ser diferente de 0.')
        except ValueError:
            print("Entrada inválida.")


if __name__ == "__main__":
   main()
