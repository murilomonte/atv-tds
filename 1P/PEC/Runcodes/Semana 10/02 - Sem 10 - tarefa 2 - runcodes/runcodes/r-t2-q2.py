def cancao():
    for i in range(99, 251):
        print(f'{i} bugs no software, pegue um deles e conserte...')
        print('Tecle "Ctrl+F5"')
        if i == 250:
            print('Vamos fazer mais um café!')

def main():
    cancao()

if __name__ == "__main__":
    main()