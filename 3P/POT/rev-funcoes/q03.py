def fah_to_cel(temp):
    return ((temp - 32) / 9) * 5


def main():
    while True:
        try:
            temp = float(input("Insira uma temperatura em fahrenheit: "))
            print(f'{temp} F° -> {fah_to_cel(temp):.2f} C°')
            break
        except:
            print("Temperatura inválida, digite novamente.")


if __name__ == "__main__":
    main()
