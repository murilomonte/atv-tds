hora = int(input("Digite as horas: "))
minuto = int(input("Digite as minuto: "))
segundo = int(input("Digite as segundo: "))

tempoDecorrido = ((hora * 60) * 60) + (minuto * 60) + segundo

print(f"Passaram-se {tempoDecorrido} segundos desde a última meia-noite.")