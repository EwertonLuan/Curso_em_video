from random import randint
print('{:=^100}'.format('\033[1;34mTentando adivinhar um número\033[m'))
numero = int(input('Tente adivinha qual número o computador escolheu: '))
computador = randint(0, 10)
palpite = 0
while not numero == computador:
    if numero < computador:
        numero = int(input('Mais... você errou tente novamente: '))
    else:
        numero = int(input('Menos...você errou tente novamente: '))
    palpite += 1

print('Parabéns você acerto o número que o computador escolheu foi {}, em {} palpites'.format(computador, palpite))
