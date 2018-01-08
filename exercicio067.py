while True:

    n = int(input('Deseja exibir a taboada de que número? '))
    print('=-'*20)
    if n < 0:
        break
    c = 1
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('=-'*20)
