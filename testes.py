from random import choice
print(' pedra [1]\n papel [2]\ntesoura\n[3]')

esco = int(input(' Escolha a sua jogada: '))
lista = ['pedra', 'papel', 'tesoura']
computa = choice(lista)

if esco == 1: #pedra
    if computa == lista[0]: # pedra
        print('computador escolheu {}, voce emptou'.format(computa))
    elif computa == lista[1]: #papel
        print('computador escolheu {}, voce perdeu'.format(computa))
    else: # tesoura
        print('Compudaro escolheu {}, voce ganhou'.format(computa))