# 9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela
# uma lista Y. A lista Y deverá conter o mesmo conteúdo da lista X na ordem inversa.


from random import randint


def invert_list(num_list: list[int]) -> list[int]:
    if type(num_list) != list:
        return Exception
    if len(num_list) == 0:
        return Exception
    # list.inverse() também funciona
    inverted_list: list[int] = []
    for num in num_list:
        inverted_list.insert(0, num)
    return inverted_list


def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 3
    random_number_list: list[int] = random_list(lenght=max_len)

    inverted_list = invert_list(num_list=random_number_list)

    print("\n## Todos os números")
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    print("\n## Lista inversa")
    print("Lista:", inverted_list)
    print("Tamanho:", len(inverted_list))


def tests() -> None:
    print("## Rodando testes")
    print("### invert_list")

    lista: list[int] = [7, 8, 0]

    assert invert_list(lista) == [0, 8, 7]
    print("- Lista com números inteiros - ok")

    assert invert_list(0) == Exception
    print("- 0 como argumento - ok")

    assert invert_list("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (invert_list(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert invert_list(True) == Exception
    print("- Booleano como argumento - ok")

    assert invert_list([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
