# 12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.


def get_somatorio(num: int) -> int:
    if type(num) != int:
        return Exception
    if num <= 0:
        return Exception
    somatorio: int = 0
    for i in range(num + 1):
        somatorio += i
    return somatorio


def tests() -> None:
    print("## Rodando testes")
    print("### get_somatorio")

    assert get_somatorio(2) == 3
    assert get_somatorio(13) == 91
    assert get_somatorio(34) == 595
    assert get_somatorio(20) == 210
    print("- Números inteiros - ok")

    assert get_somatorio(0) == Exception
    print("- 0 como argumento - ok")

    assert get_somatorio("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (get_somatorio(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert get_somatorio(True) == Exception
    print("- Booleano como argumento - ok")

    assert get_somatorio([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
