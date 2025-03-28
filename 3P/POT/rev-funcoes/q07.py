# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.

def fatorial(num: int) -> int:
    res: int = 1
    for i in range(1, num + 1):
        res *= i
    return res

def main():
    while True:
        try:
            num: int = int(input("Insira um número inteiro positivo: "))
            if num > 0:
                res: int = fatorial(num)
                print(
                    f"O fatorial de {num} é: {res}"
                )
            else:
                print('O número precisa ser diferente de 0.')
            break
        except ValueError:
            print("Entrada inválida.")


if __name__ == "__main__":
   main()