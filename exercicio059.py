import os
from time import sleep


escolha = 0
while escolha != 4:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] sair do programaz\n''')
    escolha = int(input('Escolha uma opção: '))
    if escolha == 4 :
        escolha += escolha
    n1 = int(input('Digite o primeiro valor'))
    n2 = int(input('Digite o segundo valor'))
    resultado = ''
    if escolha == 1:
        resultado = n1 + n2
    elif escolha == 2:
        resultado = n1 * n2
    elif escolha == 3:
        resultado = n1 / n2
    print('O resultado a operação é {}'.format(resultado))
    sleep(2)
    os.system('cls')

