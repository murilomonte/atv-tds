# 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5


def poligono_regular(qt_lado: int, medida_lado: int) -> dict:
    if type(qt_lado) != int or type(medida_lado) != int:
        return Exception
    if qt_lado == 3:
        perimetro: float = medida_lado * 3
        return {"tipo": "TRIÂNGULO", "calc": perimetro}
    if qt_lado == 4:
        area: float = medida_lado * medida_lado
        return {"tipo": "QUADRADO", "calc": area}
    if qt_lado == 5:
        return {"tipo": "PENTÁGONO"}
    return {"tipo": "Não é um polígono regular.", "calc": 0}


def tests() -> None:
    print("## Rodando testes")
    print("### poligono_regular")

    assert poligono_regular(3, 3) == {"tipo": "TRIÂNGULO", "calc": 9}
    print("- Número int como qt_lados e int como medida_lados - ok")

    assert (poligono_regular(1, 4)) == {"tipo": "Não é um polígono regular.", "calc": 0}
    print("- Quantidade de lados inválida (polígono não regular) - ok")

    assert poligono_regular(6.2, 6) == Exception
    print("- Número float como qt_lados - ok")

    assert poligono_regular(6, 6.2) == Exception
    print("- Número float como qt_lados - ok")

    assert poligono_regular("", "") == Exception
    print("- String como argumentos - ok")

    assert poligono_regular([], []) == Exception
    print("- List como argumentos - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
