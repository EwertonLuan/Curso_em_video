print('Todos os nuemros são impares e podem ser divididos por 3 \n')
s = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s += i
print('A soma de todos os numeros impares divisiveis por 3 é {}'.format(s))
