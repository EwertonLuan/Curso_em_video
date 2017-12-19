from random import choice
numero = [1,2,4,4,5]
usuario = int(input('Tente adivinhar qual numero que o computador vai escolher: '))
computador = choice(numero)
if computador == usuario:
    print('Parabéns você acertou')
else:
    print("Quem sabe na proxima o computardor escolheu o numero {}".format(computador))