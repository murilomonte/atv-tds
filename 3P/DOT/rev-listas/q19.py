# 19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos
# cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos
# de S. Escrever a lista X.
from random import randint


def unify_lists(list_a: list[int], list_b: list[int]) -> list[int]:
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


if __name__ == "__main__":
    main()
