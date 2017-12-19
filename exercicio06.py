
print('\033[1;34m-_-\033[m' * 30
      + '\nDescubra qual é o dobro o triplo e raiz de um numero\n'
      + '\033[1;34m-_-\033[m' * 30)

n = int(input('Didite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O dobro de {} é {} o triplo é {} e a raiz {:.1f}'.format(n, dobro, triplo, raiz))