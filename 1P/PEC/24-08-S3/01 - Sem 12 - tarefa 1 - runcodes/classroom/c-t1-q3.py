def main():
    pais1 = int(input('Insira a população do primeiro país: ').strip())
    pais2 = int(input('Insira a população do segundo país: ').strip())

    if pais1 > pais2:
        paisB = pais2
        paisA = pais1
    else:
        paisB = pais1
        paisA = pais2
    
    ano = 0

    while True:
        if paisB > paisA: break
        ano += 1
        paisA += paisA * (2/100)
        paisB += paisB * (3/100)
    
    print('A população do país B irá ultrapasar a população do país A em', ano, 'anos.')

if __name__ == '__main__':
    main()