# funçao da qst 4
def eh_primo(num):   
    cont = 0
    i = 1  
    
    while i < (num + 1):
        divisao = num % i
        if divisao == 0:
            cont += 1
        i += 1          
    if cont == 2: 
        return True
    else:
        return False    
        
def main():
    num_X = int(input('Insira o primeiro valor: '))
    num_Y = int(input('Insira o segundi valor: '))
    
    if num_X > num_Y:
        # inverter para o segundo ser sempre o maior 
        num_X = num_Y
        num_Y = num_X

    count = 0
    i = num_X
    print('Entre', num_X, 'e', num_Y, 'existem os seguintes números primos: ')
    while i <= num_Y:
        if eh_primo(i):
            print(i)
        i += 1      
    
if __name__ == "__main__":
    main()