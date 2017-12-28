print('\033[1;34m{:=^100}\033[m'.format('\33[mSomando apenas numeros pares\033[1;34m'))

c = 0
for i in range(1,7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        c = c + n
print(c)
