# 6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
# que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.
# Observação: Considere que o usuário só informará os valores 3, 4 ou 5


def poligono_regular(qt_lado: int, medida_lado: int) -> dict:
    if qt_lado == 3:
        perimetro: float = medida_lado * 3
        return {"tipo": "TRIÂNGULO", "perimetro": perimetro}
    if qt_lado == 4:
        area: float = medida_lado * medida_lado
        return {"tipo": "QUADRADO", "area": area}
    if qt_lado == 5:
        return {"tipo": "PENTÁGONO"}
    return {"tipo": "Não é um poligono regular."}


def main():
    while True:
        try:
            lados: int = int(input("Insira a quantidade de lados: "))
            if 3 <= lados <= 5:
                break
            else:
                print('Somente números 3, 4 e 5.')
        except ValueError:
            print("Opção inválida. Digite a quantidade de lados.")

    while True:
        try:
            medida: int = int(input("Insira a medida dos lados (em cm): "))
            if type(medida) == int:
                break
        except ValueError:
            print("Opção inválida. Digite a medida dos lados.")

    poligono: dict = poligono_regular(lados, medida)

    if lados == 3:
        print(f'Tipo: {poligono["tipo"]}, Perímetro: {poligono["perimetro"]}')
    if lados == 4:
        print(f'Tipo: {poligono["tipo"]}, Área: {poligono["area"]}')
    if lados == 5:
        print(f'Tipo: {poligono["tipo"]}')


if __name__ == "__main__":
    main()
