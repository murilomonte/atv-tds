# 18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para
# uma lista R, sem deixar elementos vazios entre os valores copiados. Escrever as listas X e R.
from random import randint

def transfer_list(number_list: list[int]) -> list[int]:
    list_r: list[int] = []
    for item in number_list:
        if item < 0:
            list_r.append(item)
    return list_r


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
    random_list_w: list[int] = random_list(lenght=max_len, start=-10, end=10)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    copy_list: list[int] = transfer_list(number_list=random_list_w)
    print("\n ## Lista copiada")
    print("Lista R:", copy_list)


if __name__ == "__main__":
    main()
