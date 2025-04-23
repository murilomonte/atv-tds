# 7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um
# outro valor dado pertence ou não à lista.

from random import randint


def find(item: int, list: list[int]) -> bool:
    found: bool = False
    for i in list:
        if item == i:
            found = True
            break
    return found


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
    random_list_a: list[int] = random_list(lenght=max_len)
    test_list: list[int] = random_list(lenght=max_len)

    print("\n## Todos as listas")
    print("Lista gerada:", random_list_a)
    print("Lista de comparação:", test_list)

    print("\n## Comparação")
    for i in test_list:
        print(f"{i} está na lista gerada: {find(item=i, list=random_list_a)}")


if __name__ == "__main__":
    main()
