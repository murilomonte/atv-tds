# 5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
#       - para homens : (72.7 * h) – 58
#       - para mulheres : (62.1 * h) – 44.7
# Observação: Altura = h (na fórmula acima)


def peso_ideal(altura: float, sexo: int) -> float:
    res: float = 0
    if type(altura) != float or type(sexo) != int:
        return Exception  # Poderia ser outro tipo de except
    if altura > 2.50:
        return Exception  # Poderia ser outro tipo de except
        # onde escreve o c de ecxcepct
    if sexo == 1:
        res = (72.7 * altura) - 58
        return res
    elif sexo == 2:
        res = (62.1 * altura) - 44.7
        return res
    else:
        return Exception


def tests() -> None:
    print("## Rodando testes")
    print("### peso_ideal")

    assert peso_ideal(1.75, 2) == 63.974999999999994
    print("- Número float como altura e int como sexo - ok")

    assert (peso_ideal(3, 4)) == Exception
    print("- Altura inválida - ok")

    assert (peso_ideal(1.75, 4)) == Exception
    print("- Sexo inválido - ok")

    assert peso_ideal(6, 6) == Exception
    print("- Número int como altura - ok")

    assert peso_ideal("", "") == Exception
    print("- String como argumentos - ok")

    assert peso_ideal([], []) == Exception
    print("- List como argumentos - ok")

    print("Todos os testes ok")


if __name__ == "__main__":
    tests()
