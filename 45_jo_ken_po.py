from random import choice
from time import sleep
print('\033[1;34m=+=\033[m' * 10 + '\n JO KEN PO\n' + '\033[1;34m=*=\033[m' * 10)
print('''Sua opções
[1] pedra
[2] papel 
[3] tesoura''')

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
    elif computa == lista[2]: # tesoura
        print('Compudaro escolheu {}, voce ganhou'.format(computa))
    else:
        print('Jogada inválida')
if esco == 2: #papel
    if computa == lista[0]: # pedra
        print('computador escolheu {}, voce ganhou'.format(computa))
    elif computa == lista[1]: #papel
        print('computador escolheu {}, voce empatou'.format(computa))
    elif computa == lista[2]: # tesoura
        print('Compudaro escolheu {}, voce perdeu'.format(computa))
    else:
        print('Jogada inválida')
if esco == 3: #tesoura
    if computa == lista[0]: # pedra
        print('computador escolheu {}, voce perdeu'.format(computa))
    elif computa == lista[1]: #papel
        print('computador escolheu {}, voce ganhou'.format(computa))
    elif computa == lista[2]: # tesoura
        print('Compudaro escolheu {}, voce empatou'.format(computa))
    else:
        print('Jogada inválida')