# 1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
#   a) Mostre a quantidade de números pares;
#   b) Grave uma lista somente com os números pares e mostre a lista;
#   c) Mostre a quantidade de números ímpares;
#   d) Grave uma lista somente com os números ímpares e mostre a lista.

from random import randint


def odd_even_list(number_list: list[int], isEven: bool = True) -> list[int]:
    res_list: list[int] = []
    for i in number_list:
        if isEven:
            if i % 2 == 0:
                res_list.append(i)
        else:
            if i % 2 != 0:
                res_list.append(i)
    return res_list


def random_list(lenght: int) -> list[int]:
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(0, lenght))
    return number_list


def main() -> None:
    max_len: int = 100
    print("\n## Todos os números")
    random_number_list: list[int] = random_list(max_len)
    print("Lista:", random_number_list)
    print("Tamanho:", len(random_number_list))

    print("\n## Números pares")
    even_number_list: list[int] = odd_even_list(random_number_list, isEven=True)
    print("Lista:", even_number_list)
    print("Tamanho:", len(even_number_list))

    print("\n## Números ímpares")
    even_number_list: list[int] = odd_even_list(random_number_list, isEven=False)
    print("Lista:", even_number_list)
    print("Tamanho:", len(even_number_list))


if __name__ == "__main__":
    main()
