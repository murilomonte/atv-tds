# 8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor
# mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5
from random import randint

def random_list(lenght: int, start: int = 0, end: int = 10) -> list[int]:
    """
    Generate random numbers. Default is between 0 and 10.
    """
    number_list: list[int] = []
    for _ in range(lenght):
        number_list.append(randint(start, end))
    return number_list

def calc_diferenca(a: float, b: float) -> float:
    if type(a) != float or type(b) != float:
        return Exception
    
    if a >= b: 
        return a - b
    else: 
        return b - a

def num_proximo_media(number_list: list[float]) -> float:
    if type(number_list) != list:
        return Exception
    
    if len(number_list) < 2:
        return Exception
    
    for item in number_list:
        if type(item) != float:
            return Exception

    media: float = sum(number_list) / len(number_list)
    valor_mais_proximo: float = 0
    menor_diferenca: float = calc_diferenca(media, number_list[0])

    for i in number_list:
        diferenca: float = calc_diferenca(i, media)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            valor_mais_proximo = i
            
    return valor_mais_proximo
    
def main() -> None:
    lista_original: list[float] = [10, 2.5, 7.5, 4.0]

    print(f"\nLista: {lista_original}")
    print(f"\nO valor mais próximo da média é: {num_proximo_media(lista_original)}")


def tests() -> None:
    print("## Rodando testes")
    print("### num_proximo_media")

    lista_a: list[int] = [1.0, 2.0, 3.0]
    lista_b: list[int] = [3.2, 7.4, 20.2, 5.6, 7.2, 8.9]
    
    assert num_proximo_media(lista_a) == 2.0
    assert num_proximo_media(lista_b) == 8.9

    print("- Lista com números inteiros - ok")

    assert num_proximo_media("lorem") == Exception
    print("- String qualquer como argumento - ok")

    assert (num_proximo_media(5.5)) == Exception
    print("- Número float como argumento - ok")

    assert num_proximo_media(True) == Exception
    print("- Booleano como argumento - ok")

    assert num_proximo_media([]) == Exception
    print("- List vazia como argumento - ok")

    print('### calc_diferenca')

    assert calc_diferenca(2.0, 5.0) == 3
    assert calc_diferenca(4.0, 9.0) == 5

    print("- Lista com números inteiros - ok")

    assert calc_diferenca("lorem", "ipsum") == Exception
    print("- String qualquer como argumento - ok")

    assert calc_diferenca(True, False) == Exception
    print("- Booleano como argumento - ok")

    assert calc_diferenca([], [2, 3]) == Exception
    print("- List vazia como argumento - ok")

    print("Todos os testes ok")

if __name__ == "__main__":
    tests()