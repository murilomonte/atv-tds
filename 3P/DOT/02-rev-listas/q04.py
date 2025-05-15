# 4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
# a) O maior elemento da lista e em que posição esse elemento se encontra;
# b) O menor elemento da lista e em que posição esse elemento se encontra.

from random import randint


def smaller_number(lista: list[int]) -> dict[str, int]:
    if type(lista) != list:
        return Exception
    if len(lista) == 0:
        return Exception
    smaller_number: dict[str, int] = {"num": lista[0], "index": 0}
    for index, num in enumerate(lista):
        if num < smaller_number["num"]:
            smaller_number["num"] = num
            smaller_number["index"] = index
    return smaller_number


def largest_number(lista: list[int]) -> dict[str, int]:
    if type(lista) != list:
        return Exception
    if len(lista) == 0:
        return Exception
    largest: dict[str, int] = {"num": lista[0], "index": 0}
    for index, num in enumerate(lista):
        if num > largest["num"]:
            largest["num"] = num
            largest["index"] = index
    return largest


def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 15
    random_number_list: list[int] = random_list(lenght=max_len)

    largest: dict[str, int] = largest_number(lista=random_number_list)
    smaller: dict[str, int] = smaller_number(lista=random_number_list)
    print("\n## Todos os números")
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    print("\n## Maior")
    print("Número:", largest["num"])
    print("Indice:", largest["index"])

    print("\n## Menor")
    print("Número:", smaller["num"])
    print("Indice:", smaller["index"])


def tests() -> None:
    print("## Rodando testes")
    print("### smaller_number")

    lista: list[int] = [5, 4, 1, 5, 10, 9, 6, 1, 4, 4, 10, 0, 8, 6, 5]

    assert smaller_number(lista) == {"num": 0, "index": 11}
    print("- Lista com números inteiros - ok")

    assert smaller_number(0) == Exception
    print("- 0 como argumento - ok")

    assert smaller_number("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (smaller_number(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert smaller_number(True) == Exception
    print("- Booleano como argumento - ok")

    assert smaller_number([]) == Exception
    print("- List vazia como argumento - ok")

    print("### largest_number")

    assert largest_number(lista) == {"num": 10, "index": 4}
    print("- Lista com números inteiros - ok")

    assert largest_number(0) == Exception
    print("- 0 como argumento - ok")

    assert largest_number("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (largest_number(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert largest_number(True) == Exception
    print("- Booleano como argumento - ok")

    assert largest_number([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()