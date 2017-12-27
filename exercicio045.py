print('\033[1;34m=+=\033[m' * 10 + '\n JO KEN PO\n' + '\033[1;34m=*=\033[m' * 10)
from random import choice
from time import sleep
print(' pedra [1]\n papel [2]\ntesoura[3]\n')

esco = int(input(' Escolha a sua jogada: '))
lista = ['pedra', 'papel', 'tesoura']
computa = choice(lista)
print('\033[1;36mJO KEN PO...\033[m')
sleep(2)
if esco == 1: #pedra
    if computa == lista[0]: #pedra
        print('computador escolheu {}, voce emptou'.format(computa))
    elif computa == lista[1]: #papel
        print('computador escolheu {}, voce perdeu'.format(computa))
    else: # tesoura
        print('Compudaro escolheu {}, voce ganhou'.format(computa))
if esco == 2: #papel
    if computa == lista[0]: # pedra
        print('computador escolheu {}, voce ganhou'.format(computa))
    elif computa == lista[1]: #papel
        print('computador escolheu {}, voce empatou'.format(computa))
    else: # tesoura
        print('Compudaro escolheu {}, voce perdeu'.format(computa))
if esco == 3: #tesoura
    if computa == lista[0]: # pedra
        print('computador escolheu {}, voce perdeu'.format(computa))
    elif computa == lista[1]: #papel
        print('computador escolheu {}, voce ganhou'.format(computa))
    else: # tesoura
        print('Compudaro escolheu {}, voce empatou'.format(computa))