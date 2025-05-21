# 6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True
# caso a lista esteja ordenada em ordem ascendente ou False caso não esteja
# ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False

from random import randint

def ordered(number_list: list[int]) -> bool:
    if type(number_list) != list:
        return Exception
    
    if len(number_list) < 2:
        return Exception
    
    for item in number_list:
        if type(item) != int:
            return Exception
    
    for index in range(1, len(number_list)):
        if number_list[index - 1] > number_list[index]: return False
    return True

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

    print("\n## Lista gerada")
    print("Lista X:", random_list_w)

    print("\n## Resultado final")
    print("A lista está ordenada?", ordered(random_list_w))

def tests() -> None:
    print("## Rodando testes")
    print("### ordered")

    lista_a: list[int] = [1, 2, 3]
    lista_b: list[int] = [3, 7, 20, 5, 7, 8]
    
    assert ordered(lista_a) == True
    assert ordered(lista_b) == False

    print("- Lista com números inteiros - ok")

    assert ordered("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (ordered(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert ordered(True) == Exception
    print("- Booleano como argumento - ok")

    assert ordered([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")

if __name__ == "__main__":
    tests()
