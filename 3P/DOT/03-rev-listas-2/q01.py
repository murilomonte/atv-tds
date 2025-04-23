# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

from random import randint

def del_duplicates(number_list: list[int]) -> list[int]:
    buffer_list: list[int] = []
    for item in number_list:
        if item not in buffer_list:
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
    random_list_w: list[int] = random_list(lenght=max_len)

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    new_list = del_duplicates(number_list=random_list_w)

    print("\n## Lista sem duplicatas")
    print("Lista:", new_list)

    # TODO: fazer testes

if __name__ == "__main__":
    main()