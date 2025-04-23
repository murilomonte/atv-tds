# 15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem
# inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim
# por diante. Escrever todo a lista D e todo a lista E.


from random import randint


def invert_list(num_list: list[int]) -> list[int]:
    # list.inverse() também funciona
    inverted_list: list[int] = []
    for num in num_list:
        inverted_list.insert(0, num)
    return inverted_list


def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list


def main() -> None:
    max_len: int = 15
    random_number_list: list[int] = random_list(lenght=max_len)

    inverted_list = invert_list(num_list=random_number_list)

    print("\n## Todos os números")
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    print("\n## Lista inversa")
    print("Lista:", inverted_list)
    print("Tamanho:", len(inverted_list))

if __name__ == "__main__":
    main()
