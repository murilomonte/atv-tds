celcius = float(input('Insira os graus em Celcius: '))

def convFahrenheit(celcius):
    return (celcius * (9/5)) + 32

print(f'{celcius}C° são {convFahrenheit(celcius):.2f}F°')