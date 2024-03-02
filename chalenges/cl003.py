num = int(input("Digite um número: "))

# foi necessario a utilização da funcao pow() para calcular raizes iracionais
print (' Dobro: {}\n Triplo: {}\n Raiz quadrada {:.5f}'.format(num * 2, num * 3, pow(num, 1/2)))
