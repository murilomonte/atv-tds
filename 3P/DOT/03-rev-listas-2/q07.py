# 7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso algum elemento apareça mais de uma vez ou False caso nenhum elemento
# apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False

from random import randint

def ocurrence(number_list: list[int]) -> bool:
    for number in number_list:
        ocurrences: int = 0
        for number_comparasion in number_list:
            if number == number_comparasion: 
                ocurrences += 1
        if ocurrences > 1: return True
    return False


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
    # random_list_w: list[int] = [3, 7, 2, 4]
    

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    print("\n## Resultado final")
    print("Algum elemento aparece mais vezes na lista:", ocurrence(random_list_w))

if __name__ == "__main__":
    main()