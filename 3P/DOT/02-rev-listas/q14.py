# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.

from random import randint


def replace_numbers(number_list: list[int]) -> list[int]:
    if type(number_list) != list:
        return Exception
    if len(number_list) == 0:
        return Exception
    modified_list: list[int] = number_list
    for index, item in enumerate(number_list):
        if item < 0:
            number_list.remove(item)
            number_list.insert(index, 0)
    return modified_list


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
    random_number_list: list[int] = random_list(lenght=max_len, start=-10, end=10)

    print("\n## Todos os números")
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    modified_list: list[int] = replace_numbers(number_list=random_number_list)
    print("\n## Números negativos trocados")
    print(f"Lista: {modified_list}")


def tests() -> None:
    print("## Rodando testes")
    print("### replace_numbers")

    lista: list[int] = [-8, -10, -7, -8, 0, 5, -7, -2, -7, 3]

    assert replace_numbers(lista) == [0, 0, 0, 0, 0, 5, 0, 0, 0, 3]
    print("- Gabarito e respostas corretos - ok")

    assert replace_numbers(0) == Exception
    print("- 0 como argumento - ok")

    assert replace_numbers("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (replace_numbers(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert replace_numbers(True) == Exception
    print("- Booleano como argumento - ok")

    assert replace_numbers([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()

