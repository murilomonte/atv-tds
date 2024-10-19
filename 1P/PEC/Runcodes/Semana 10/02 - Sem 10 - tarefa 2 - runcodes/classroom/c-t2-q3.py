def cancao():
    for i in range(99, 251, 7):
        print(f'{i} bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')
        if i == 246:
            print('Vamos fazer mais um café!')

def main():
    cancao()

if __name__ == "__main__":
    main()