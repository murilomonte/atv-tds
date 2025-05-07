# 9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] = [7, 3]

from random import randint


def ocurrence(number_list: list[int]) -> list[int]:
    buffer_list: list[int] = []
    for number in number_list:
        ocurrences: int = 0
        for number_comparasion in number_list:
            if number == number_comparasion:
                ocurrences += 1
        if ocurrences == 1:
            buffer_list.append(number)
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
    max_len: int = 4
    random_list_w: list[int] = random_list(lenght=max_len)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    print("\n## Resultado final")
    print("Lista sem números que repetem:", ocurrence(random_list_w))


if __name__ == "__main__":
    main()
