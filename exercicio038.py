print('\033[1;34m=+\033[m' * 10 + '\nComparando numeros\n' + '\033[1;34m=+\033[m' * 10)
n_1 = int(input('Digite o primeiro numero: '))
n_2 = int(input('Digite o segundo numero: '))

if n_1 > n_2:
    print('O primeiro valor {} e maior que o segundo valor {}'.format(n_1, n_2))
elif n_1 == n_2:
    print('{} é igual a {}'.format(n_1, n_2))
else:
    print('{} é maior que {}'.format(n_2, n_1))
