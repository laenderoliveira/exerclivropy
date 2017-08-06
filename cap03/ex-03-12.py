distancia = float(input("Distancia em Km: "))
velocidade = float(input("Velocidade Média em Km/h: "))
tempo = distancia / velocidade
tempo_s = tempo * 3600
horas = tempo_s // 3600
tempo_s = tempo_s % 3600
minutos = tempo_s // 60
segundos = tempo_s % 60
print("O tempo de viagem é %02d:%02d:%02d" % (horas, minutos, segundos))
