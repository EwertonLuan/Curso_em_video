print('{:=^50}'.format('Descobrindo um numero primo'))
c = 0
num = int(input('\nDigite um numero: '))
for i in range (2, num):
    if num % i == 0 and c < 2:
        c += 1
        print(i)
if c == 0:
    print('O numero {} é um numero primo'.format(num))
else:
    print('O numero {} não é primo'.format(num))

