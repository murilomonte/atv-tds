def area(raio) -> float:
    return 3.14 * raio**2


def perimetro(raio) -> float:
    return 3.14 * 2 * raio


def main():
    while True:
        try:
            raio = float(input("Insira o raio do círculo: "))
            print(f'A área do círculo é: {area(raio)}')
            print(f'O perímetro do círculo é: {perimetro(raio)}')
            break
        except:
            print("Número inválido. Digite novamente!")


if __name__ == "__main__":
    main()
