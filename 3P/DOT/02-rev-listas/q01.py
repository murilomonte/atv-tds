# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
#   a) Mostre a quantidade de números pares;
#   b) Grave uma lista somente com os números pares e mostre a lista;
#   c) Mostre a quantidade de números ímpares;
#   d) Grave uma lista somente com os números ímpares e mostre a lista.

from random import randint


def odd_even_list(number_list: list[int], isEven: bool = True) -> list[int]:
    if type(number_list) != list or type(isEven) != bool:
        return Exception
    if len(number_list) == 0:
        return Exception
    res_list: list[int] = []
    for i in number_list:
        if i < 0:
            return Exception
        if isEven:
            if i % 2 == 0:
                res_list.append(i)
        else:
            if i % 2 != 0:
                res_list.append(i)
    return res_list


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
    print("\n## Todos os números")
    random_number_list: list[int] = random_list(max_len)
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    print("\n## Números pares")
    even_number_list: list[int] = odd_even_list(random_number_list, isEven=True)
    print("Lista:", even_number_list)
    print("Tamanho:", len(even_number_list))

    print("\n## Números ímpares")
    even_number_list: list[int] = odd_even_list(random_number_list, isEven=False)
    print("Lista:", even_number_list)
    print("Tamanho:", len(even_number_list))


def tests() -> None:
    print("## Rodando testes")
    print("### odd_even_list")

    lista: list[int] = [9, 7, 8, 0, 0, 0, 5, 5, 1, 10]

    assert odd_even_list(lista, isEven=True) == [8, 0, 0, 0, 10]
    assert odd_even_list(lista, isEven=False) == [9, 7, 5, 5, 1]
    print("- Lista com números inteiros - ok")

    assert odd_even_list(0) == Exception
    print("- 0 como argumento - ok")

    assert odd_even_list("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (odd_even_list(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert odd_even_list(True) == Exception
    print("- Booleano como argumento - ok")

    assert odd_even_list([]) == Exception
    print("- List como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
