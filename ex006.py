from math import sqrt

catOp = float(input("digite o cateto oposto: "))
catAd = float(input("digite o cateto adjacente: "))

hip = sqrt(pow(catOp, 2) + pow(catAd, 2))

print("Valor da hipotenusa: {}".format(hip))