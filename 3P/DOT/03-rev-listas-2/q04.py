# 4) Escreva uma função que recebe uma lista com n números inteiros, e determina a
# maior soma de qualquer seguimento da lista. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 34

from random import randint

def algoritmo_linear(number_list: list[int]) -> int:
    if type(number_list) != list:
        return Exception
    
    if len(number_list) < 2:
        return Exception
    
    for item in number_list:
        if type(item) != int:
            return Exception

    max_soma_interna = number_list[0]
    max_soma_global = number_list[0]

    ## Para cada número da number_list, testa se o mesmo é maior que a soma do anterior com ele mesmo
    for num in number_list[1:]:
        max_soma_interna = max(num, max_soma_interna + num) # Escolhe se deve continuar somando ou deve substituir o valor
        max_soma_global = max(max_soma_global, max_soma_interna) # Se a soma da sublista for maior, troca o valor global
    
    return max_soma_global


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

    largest_sum: int = algoritmo_linear(lista=random_list_w)
    print("\n# Maior soma")
    print(f"Valor: {largest_sum}")

def tests() -> None:
    print("## Rodando testes")
    print("### algoritmo_linear")

    lista_a: list[int] = [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1]
    
    assert algoritmo_linear(lista_a) == 34

    print("- Lista com números inteiros - ok")

    assert algoritmo_linear("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (algoritmo_linear(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert algoritmo_linear(True) == Exception
    print("- Booleano como argumento - ok")

    assert algoritmo_linear([]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")

if __name__ == "__main__":
    tests()
