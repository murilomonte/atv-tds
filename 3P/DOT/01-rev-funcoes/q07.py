# 7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por
# sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize
# uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste
# número, também do tipo inteiro.

def fatorial(num: int) -> int:
    if type(num) != int:
        return Exception
    if num < 0:
        return Exception
    res: int = 1
    for i in range(1, num + 1):
        res *= i
    return res


def tests() -> None:
    print("## Rodando testes")
    print("### fatorial")

    assert fatorial(5) == 120
    assert fatorial(0) == 1
    print("- Número int como argumento - ok")

    assert fatorial(-1) == Exception

    assert (fatorial(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert fatorial("") == Exception
    print("- String como argumento - ok")

    assert fatorial([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
