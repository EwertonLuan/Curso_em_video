from datetime import date
print('{:#^50}\n'.format('Verificadno a maioridade'))
anos = []
atual = date.today().year
maior = 0
menor = 0

for i in range(0, 7):
    idade = int(input('Idade'))
    c = anos.append(idade)

for e in anos:
    if atual - e >= 18:
        print('maior de idade {}'.format(e))
        maior += 1
    else:
        print('menor de idade{}'.format(e))
        menor += 1

print('{} pessoas são maior de idade é {} são menor de idade'.format(maior, menor))
