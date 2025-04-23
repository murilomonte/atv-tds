# 3) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 25

from random import randint

def determine_sum(number_list: list[int]) -> int:
    largest_sum: int = 0
    for index in range(len(number_list)):
        if index < len(number_list):
            if number_list[index] + number_list[index + 1] > largest_sum:
                largest_sum = number_list[index] + number_list[index]
    return largest_sum

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

    largest_sum: int = determine_sum(number_list=random_list_w)
    print('\n# Maior soma')
    print(f'Valor: {largest_sum}')

if __name__ == "__main__":
    main()