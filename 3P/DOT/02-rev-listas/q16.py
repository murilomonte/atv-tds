# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# Escrever as listas X e Y.


from random import randint


def calc(list_a: list[int]) -> list[float]:
    if type(list_a) != list:
        return Exception
    if len(list_a) == 0:
        return Exception
    
    buffer_list: list[float] = []
    for index, item in enumerate(list_a):
        if index % 2 == 0:
            buffer_list.append(item / 2)
        else:
            buffer_list.append(item * 3)

    return buffer_list

def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 10
    random_list_x: list[int] = random_list(lenght=max_len)

    print("\n## Lista gerada")
    print("Lista X:", random_list_x)

    modified_list: list[float] = calc(random_list_x)

    print("\n## Lista modificada")
    print("Lista Y:", modified_list)


def tests() -> None:
    print("## Rodando testes")
    print("### calc")

    lista: list[int] = [5, 2, 2, 7, 2, 10, 8, 7, 7, 7]

    assert calc(lista) == [2.5, 6, 1.0, 21, 1.0, 30, 4.0, 21, 3.5, 21]
    print("- Lista com números inteiros - ok")

    assert calc(0) == Exception
    print("- 0 como argumento - ok")

    assert calc("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (calc(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert calc(True) == Exception
    print("- Booleano como argumento - ok")

    assert calc([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
