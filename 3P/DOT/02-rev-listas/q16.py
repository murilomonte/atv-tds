# 16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os
# elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os
# elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# Escrever as listas X e Y.


from random import randint


def calc(list_a: list[int]) -> list[float]:
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



if __name__ == "__main__":
    main()