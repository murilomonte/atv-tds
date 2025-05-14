# 13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
# S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.


def calc(n: int) -> float:
    if type(n) != int:
        return Exception
    if n <= 0:
        return Exception
    res: float = 0
    for i in range(1, n + 1):
        res += 1 / i
    return res


def tests() -> None:
    print("## Rodando testes")
    print("### calc")

    assert calc(5) == 2.283333333333333
    assert calc(56) == 4.611469354783229
    assert calc(3) == 1.8333333333333333
    assert calc(9) == 2.8289682539682537
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
