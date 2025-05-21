# 1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma
# lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]

from random import randint

def del_duplicates(number_list: list[int]) -> list[int]:
    if type(number_list) != list:
        return Exception
    
    if len(number_list) < 2:
        return Exception
    
    for item in number_list:
        if type(item) != int:
            return Exception
    
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


def tests() -> None:
    print("## Rodando testes")
    print("### del_duplicates")

    lista_a: list[int] = [9, 2, 0, 4, 7, 0, 6, 2, 0, 1]

    assert del_duplicates(lista_a) == [9, 2, 0, 4, 7, 6, 1]
    print("- Lista com números inteiros - ok")

    assert del_duplicates("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (del_duplicates(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert del_duplicates(True) == Exception
    print("- Booleano como argumento - ok")

    assert del_duplicates([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")

if __name__ == "__main__":
    tests()
