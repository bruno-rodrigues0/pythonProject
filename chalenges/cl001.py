x = input('Digite algo: ')

print(' Tipo primitivo: {}\n'
      ' Numérico: {}\n'
      ' Alfabético: {}\n'
      ' Alfanumérico: {}\n'
      ' Upper case: {}\n'
      ' Lower case: {}'
      .format(type(x), x.isnumeric(), x.isalpha(), x.isalnum(), x.isupper(), x.islower()))
