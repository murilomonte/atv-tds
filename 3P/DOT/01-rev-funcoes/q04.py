def calc_nota(n1: float, n2: float) -> float:
    if type(n1) != float:
        return Exception
    media: float = (n1 + n2) / 2
    return media


def tests() -> None:
    print("## Rodando testes")
    print("### fah_to_cel")
    assert calc_nota(6.0, 6.0) == 6.0
    print("- Número float como argumento - ok")

    assert calc_nota(6, 6) == Exception
    print("- Número int como argumento - ok")

    assert calc_nota("", "") == Exception
    print("- String como argumento - ok")

    assert calc_nota([], []) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
