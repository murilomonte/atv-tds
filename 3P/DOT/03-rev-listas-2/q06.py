# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

from random import randint

def ordered(number_list: list[int]) -> bool:
    for index in range(1, len(number_list)):
        if number_list[index - 1] > number_list[index]: return False
    return True


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
    print("A lista está ordenada?", ordered(random_list_w))

if __name__ == "__main__":
    main()