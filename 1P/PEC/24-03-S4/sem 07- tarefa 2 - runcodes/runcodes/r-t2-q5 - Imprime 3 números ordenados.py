num1 = int(input('').strip())
num2 = int(input('').strip())
num3 = int(input('').strip())

def cresc(num1, num2, num3):
    ind1 = max(num1, num2, num3)
    ind3 = min(num1, num2, num3)
    ind2 = (num1 + num2 + num3) - (ind1 + ind3)
    return f'{ind3}\n{ind2}\n{ind1}'

print(f'{cresc(num1, num2, num3)}')