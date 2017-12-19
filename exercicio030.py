num = int(input('Digite um numero: '))
par = num % 2
if par == 0:
    print('O numero {} e par'.format(num))
else:
    print('O numero {} é impar'.format(num))