# Aqui deve-se colocar a quantidade de segundos desejado
total_seg = int(input("Segundos:"))

# Cálculo de horas, minutos e segundos
horas = total_seg // 3600
restante_seg = total_seg % 3600
minutos = restante_seg // 60
seg_finais = restante_seg % 60

print(f"{total_seg} segundos equivalem a:")
print(f"{horas}h {minutos}m {seg_finais}s")
# Aqui deve ocorrer o inverso do primeiro codigo, aqui deve-se digitar as horas, minutos e segundos para transformar tudo em segundos.
h = int(input("horas: "))
m = int(input("minutos: "))
s = int(input("segundos: "))

# Cálculo do total
total_convertido = (h * 3600) + (m * 60) + s

print(f"O tempo total é de {total_convertido} segundos.")
