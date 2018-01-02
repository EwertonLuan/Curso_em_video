from datetime import date
print('{:#^50}\n'.format('Verificadno a maioridade'))
atual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    pessoas = int(input('No de nacismento de {}º pessoa'.format(i)))
    if atual - pessoas >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são maior de idade é {} são menor de idade'.format(maior, menor))
