print('{:*^50}\n'.format('Decobrindo o mais pesado é o mais leve'))
li = []
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}ª em kg'.format(pessoa)))
    c = li.append(peso)

print('A pessoa mais pesada tem {}kg e a mais leve {}kg'.format(max(li), min(li)))

# outra forma de resolução do problema
"""
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso em kg da {}ª pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa mais pesada tem {}kg e a mais leve {}kg'.format(maior, menor))
"""