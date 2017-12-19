n_1 = float(input('Digite o primeiro numero: '))
n_2 = float(input('Digite o segundo numero: '))
n_3 = float(input('Digite o terceiro numero: '))

if n_1 > n_2 and n_1 > n_3:
    print('Ele é o maior {}'.format(n_1))
elif n_2 > n_1 and n_2 > n_3:
    print('Ele é o maior {}'.format(n_2))
elif n_3 > n_1 and n_3 > n_2:
    print('Ele é o maior {}'.format(n_3))

if n_1 < n_2 and n_1 < n_3:
    print('Ele é o memor {}'.format(n_1))
elif n_2 < n_1 and n_2< n_3:
    print('Ele é o memor {}'.format(n_2))
elif n_3 < n_1 and n_3 < n_2:
    print('Ele é o menor {}'.format(n_3))



