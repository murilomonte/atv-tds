# 14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + 1/1! + ½! + 1/3! + 1 /N!


def calc(n: int) -> float:
    if type(n) != int:
        return Exception
    if n <= 0:
        return Exception
    res: float = 0
    for i in range(1, n + 1):
        res += 1 / fatorial(i)
    return res


def fatorial(num: int) -> float:
    if type(num) != int:
        return Exception
    if num <= 0:
        return Exception
    res: float = 1
    for i in range(1, num + 1):
        res *= i
    return res


def tests() -> None:
    print("## Rodando testes")
    print("### calc")

    assert calc(5) == 1.7166666666666668
    assert calc(56) == 1.7182818284590455
    assert calc(3) == 1.6666666666666667
    assert calc(9) == 1.7182815255731925
    print("- Números inteiros - ok")

    assert calc(0) == Exception
    print("- 0 como argumento - ok")

    assert calc("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (calc(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert calc(True) == Exception
    print("- Booleano como argumento - ok")

    assert calc([]) == Exception
    print("- List como argumento - ok")

    print("### fatorial")

    assert fatorial(5) == 120
    assert fatorial(4) == 24
    assert fatorial(3) == 6
    assert fatorial(2) == 2
    print("- Números inteiros - ok")

    assert fatorial(0) == Exception
    print("- 0 como argumento - ok")

    assert fatorial("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (fatorial(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert fatorial(True) == Exception
    print("- Booleano como argumento - ok")

    assert fatorial([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
