# 15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)


def calc(n: int) -> float:
    if type(n) != int:
        return Exception
    if n <= 0:
        return Exception
    res: float = 0
    for i in range(1, n + 1):
        res += ((i**2) + 1) / (i + 3)
    return res


def tests() -> None:
    print("## Rodando testes")
    print("### calc")
    
    assert calc(5) == 8.845238095238095
    assert calc(9) == 30.698773448773448
    assert calc(3) == 3.166666666666667
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

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
