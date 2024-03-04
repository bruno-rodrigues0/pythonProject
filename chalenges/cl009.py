lar = float(input("Digite a largura da parede"))
alt = float(input("Digite a altura da parede"))

area = lar*alt
tintaNec = area/2

print("A area da parede eh {} e eh necessario {} litros de tinta para pinta-la".format(area, tintaNec))