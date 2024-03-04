import random

alunos = ['joao', 'maria',  'jose', 'madalena']
seq = []

for i in range(3):
    seq[i] = random.randint(0,3)
    print("{}, ".format(seq[i]))    