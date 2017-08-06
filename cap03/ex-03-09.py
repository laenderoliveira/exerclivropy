dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total = segundos + minutos * 60 + horas * 3600 + dias * 24 * 3600
print("Total em segundos: %d " % total)