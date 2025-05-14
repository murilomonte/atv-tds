def area(raio) -> float:
    if type(raio) != float:
        return Exception
    res: float = 3.14 * raio**2
    return res


def perimetro(raio) -> float:
    if type(raio) != float:
        return Exception
    res: float = 3.14 * 2 * raio
    return res


def tests() -> None:
    print("## Rodando testes")
    print("### Area")
    assert area(3.0) == 28.26
    print("- Número float como argumento - ok")

    assert area(1) == Exception
    print("- Número inteiro como argumento - ok")

    assert area([1]) == Exception
    print("- Lista de números como argumento - ok")

    assert area("a") == Exception
    print("- String como argumento - ok")

    print("### Perimetro")
    assert perimetro(3.0) == 18.84
    print("- Número float como argumento - ok")

    assert perimetro(1) == Exception
    print("- Número inteiro como argumento - ok")

    assert perimetro([1]) == Exception
    print("- Lista de números como argumento - ok")

    assert perimetro("a") == Exception
    print("- String como argumento - ok")

    print("Todos os testes - ok ")


if __name__ == "__main__":
    tests()
