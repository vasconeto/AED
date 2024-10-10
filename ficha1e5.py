seconds = int(input("Indique o tempo em segundos: "))
hours = int((seconds/60)/60)
minutes = int((seconds/60)%60)
seconds_2 = int(seconds%60)

print("%d horas, %d minutos, %d segundos" % (hours, minutes, seconds_2))