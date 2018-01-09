from random import randint

ganhou = 0
while True:
    pi = str(input('Escolha P(par) ou I(impar): ')).upper().strip()
    while pi not in 'PI':
        pi = str(input('Escolha P(par) ou I(impar): ')).upper().strip()
    n = int(input('Digite o um numero: '))
    if pi == 'P':
        cpu = 'I'
    else:
        cpu = 'P'
    cpu_num = randint(1, 10)
    soma = cpu_num + n
    par = ''
    impar = ''

    if soma % 2 == 0:
        par = 'P'
        s_pi = 'PAR'
    else:
        impar = 'I'
        s_pi = 'IMPAR'
    print(f'Você jogou {n} e o computador {cpu_num} somando {soma} DEU {s_pi}')
    if pi == par or pi == impar:
        print('Você ganhou')
        ganhou += 1
    else:
        print('Você perdeu')
        break
print(f'Voce ganhou {ganhou} e a maquina escolheu {s_pi} na ultima')
