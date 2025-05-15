# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
# de S. Escrever a lista X.
from random import randint


def unify_lists(list_a: list[int], list_b: list[int]) -> list[int]:
    if type(list_a) != list or type(list_b) != list:
        return Exception
    if len(list_a) == 0 or len(list_b) == 0:
        return Exception
    ## list.extend também funciona
    buffer_list: list[int] = list_a

    for item in list_b:
        buffer_list.append(item)

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
    random_list_r: list[int] = random_list(lenght=max_len)
    random_list_s: list[int] = random_list(lenght=max_len)

    print("\n## Listas geradas")
    print("Lista R:", random_list_r)
    print("Lista R:", random_list_s)

    unified_list = unify_lists(list_a=random_list_r, list_b=random_list_s)
    print("\n## Listas unificadas")
    print("Lista unificada:", unified_list)



def tests() -> None:
    print("## Rodando testes")
    print("### unify_lists")

    lista_a: list[int] = [9, 2, 0, 4, 7, 0, 6, 2, 0, 1]
    lista_b: list[int] = [5, 5, 9, 0, 9, 2, 5, 0, 1, 5]

    assert unify_lists(lista_a, lista_b) == [9, 2, 0, 4, 7, 0, 6, 2, 0, 1, 5, 5, 9, 0, 9, 2, 5, 0, 1, 5]
    print("- Lista com números inteiros - ok")

    assert unify_lists("lorem", "ipsum") == Exception
    print("- String qualquer como argumento - ok")

    assert (unify_lists(5.5, 4.6)) == Exception
    print("- Número float como argumento - ok")

    assert unify_lists(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert unify_lists([], []) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
