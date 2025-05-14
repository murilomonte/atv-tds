def num_par(num: int) -> bool | Exception:
    if type(num) == int:
        if num % 2 == 0:
            return True
        return False
    return Exception


def tests() -> None:
    print("## Rodando testes")

    assert num_par(2) == True
    print("- Número par como argumento - ok")

    assert num_par(1) == False
    print("- Número ímpar como argumento - ok")

    assert num_par("") == Exception
    print("- String como argumento - ok")

    assert num_par(2.0) == Exception
    print("- Número float como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
