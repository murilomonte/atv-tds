# 14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0.
# Escrever a lista C modificada.


from random import randint


def replace_numbers(number_list: list[int]) -> list[int]:
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


if __name__ == "__main__":
    main()