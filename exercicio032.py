ano = int(input('Digite um ano: '))
bissexto = int(ano % 4)
secular = int(ano % 100)
tempo = float((float(ano) / 100)%4)
print(tempo)

if bissexto == 0 and secular != 0 and tempo != 0.0:
    print('O ano de {} é sum ano bisexto'.format(ano))
else:
    print('O ano {} não é um ano bisexto'.format(ano))
