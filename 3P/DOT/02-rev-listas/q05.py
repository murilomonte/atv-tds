# 5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
# elementos deste em uma outra lista de 20 elementos.
from random import randint


def intercalate(list_a: list[int], list_b: list[int]) -> list[int]:
    if (type(list_a) != list) or (type(list_b) != list):
        return Exception
    if (len(list_a) == 0) or (len(list_b) == 0):
        return Exception
    if len(list_a) == len(list_b):
        buffer_list: list[int] = []
        for index in range(len(list_a)):
            buffer_list.append(list_a[index])
            buffer_list.append(list_b[index])
        return buffer_list
    else:
        return Exception


def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 5
    random_list_a: list[int] = random_list(lenght=max_len)
    random_list_b: list[int] = random_list(lenght=max_len)

    res: list[int] = intercalate(list_a=random_list_a, list_b=random_list_b)
    print("\n## Todos as listas")
    print("Lista A:", random_list_a)
    print("Lista B:", random_list_b)

    print("\n## Resultado")
    print("Lista intercalada:", res)
    print("Tamanho da lista:", len(res))


def tests() -> None:
    print("## Rodando testes")
    print("### intercalate")

    lista_a: list[int] = [5, 3, 3, 4, 1]
    lista_b: list[int] = [2, 8, 7, 3, 4]

    assert intercalate(lista_a, lista_b) == [5, 2, 3, 8, 3, 7, 4, 3, 1, 4]
    print("- Lista com números inteiros - ok")

    assert intercalate([1], [2, 2, 4]) == Exception
    print("- Lista com listas de tamanho diferente - ok")

    assert intercalate(0, 0) == Exception
    print("- 0 como argumento - ok")

    assert intercalate("lorem", 'ipsum') == Exception
    print("- String qualquer como argumento - ok")

    assert (intercalate(5.5, 5.4)) == Exception
    print("- Número float como argumento - ok")

    assert intercalate(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert intercalate([], []) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
