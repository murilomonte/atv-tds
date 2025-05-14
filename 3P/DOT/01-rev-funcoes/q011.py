# 11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.


def get_divisores(num: int) -> list[int]:
    if type(num) != int:
        return Exception
    if num <= 0:
        return Exception
    divisores: list[int] = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


def tests() -> None:
    print("## Rodando testes")
    print("### get_divisores")

    assert get_divisores(13) == [1, 13]
    assert get_divisores(34) == [1, 2, 17, 34]
    assert get_divisores(20) == [1, 2, 4, 5, 10, 20]
    print("- Números inteiros - ok")

    assert get_divisores(0) == Exception
    print("- Divisão por zero - ok")

    assert get_divisores("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (get_divisores(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert get_divisores(True) == Exception
    print("- Booleano como argumento - ok")

    assert get_divisores([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
