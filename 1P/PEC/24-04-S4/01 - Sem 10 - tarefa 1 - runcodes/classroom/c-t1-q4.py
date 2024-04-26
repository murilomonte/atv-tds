def sequencia():
    seq = ''
    num = 0
    for i in range(100):
        num += 10
        if num != 1000:
            seq += f'{num}, '
        else:
            seq += f'{num}.'
    return seq

def main ():
    print(sequencia())

if __name__ == "__main__":
    main()