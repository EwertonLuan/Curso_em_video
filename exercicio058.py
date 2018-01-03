from random import randint

numero = int(input('Tente adivinha qual número o computador escolheu: '))
computador = randint(0, 10)
palpite = 0
while not numero == computador:
    numero = int(input('Voce errou tente novamente: '))
    palpite += 1
print('Parabens você acerto o número que o computador escolheu foi {}, em {} palpites'.format(computador, palpite))
