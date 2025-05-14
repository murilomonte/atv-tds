def fah_to_cel(temp: float) -> float:
    if type(temp) != float:
        return Exception
    res: float = ((temp - 32) / 9) * 5
    return res


def tests() -> None:
    print("## Rodando testes")
    print("### fah_to_cel")
    assert fah_to_cel(32.0) == 0
    print("- Número float como argumento - ok")

    assert fah_to_cel(12) == Exception
    print("- Número int como argumento - ok")

    assert fah_to_cel("") == Exception
    print("- String como argumento - ok")

    assert fah_to_cel([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
