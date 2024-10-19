def cancao():
    for i in range(99, 0, -11):
        print(f'{i} bugs no software, pegue onze deles e conserte...')
        print('Tecle "Ctrl+F5"')
        if i == 11:
            print('Sem erros no software! Está estabilizado!')

def main():
    cancao()

if __name__ == "__main__":
    main()