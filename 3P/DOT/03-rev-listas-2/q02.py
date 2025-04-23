# 2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime
# o número de vezes que cada número ocorre na sequência.
from random import randint


def number_counter(number_list: list[int]) -> dict[int, int]:
    buffer_dict: dict[int, int] = {}
    for item in number_list:
        if item in buffer_dict:
            for key in buffer_dict:
                if item == key:
                    buffer_dict[key] += 1
        else:
            buffer_dict.update({item: 1})

    return buffer_dict


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
    random_list_w: list[int] = random_list(lenght=max_len)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    number_counter_list: dict[int, int] = number_counter(number_list=random_list_w)

    print("\n## Número de ocorrências")
    for key in number_counter_list:
        print(
            f"O número {key} apareceu {number_counter_list[key]}",
            "vez" if number_counter_list[key] == 1 else "vezes",
        )
        # print(f'{key} -> {number_counter_list[key]}')

    # TODO: fazer testes


if __name__ == "__main__":
    main()
