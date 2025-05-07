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
    if a >= b: 
        return a - b
    else: 
        return b - a

def num_proximo_media(lista: list[float]) -> float:
    media: float = sum(lista) / len(lista)
    valor_mais_proximo: float = 0
    menor_diferenca: float = calc_diferenca(media, lista[0])

    for i in lista:
        diferenca: float = calc_diferenca(i, media)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            valor_mais_proximo = i
            
    return valor_mais_proximo
    
def main() -> None:
    lista_original: list[float] = [10, 2.5, 7.5, 4.0]

    print(f"\nLista: {lista_original}")
    print(f"\nO valor mais próximo da média é: {num_proximo_media(lista_original)}")

if __name__=='__main__':
    main()