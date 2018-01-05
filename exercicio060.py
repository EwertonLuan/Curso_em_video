t = int (input('Digite um numero: '))
n = t
n1 = n-1
f = ''
c = 0
for i in range(1,t+1):
    f = str(i) + ' ' + f
while c != n1:
    if n1 >= 1:
        n = n1 * n
        n1 -= 1
       # print(n)

print('Cauculando... {}! = {} = {}'.format(t, f.strip().replace(' ', ' x '), n))
# Ou conforme a correção
'''
n = int(input('Difite um numero para ser fatorado: '))
c = n
f = 1
print('Cauculando o valor {}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='') # Vai printar o ex: 5 4 3 2 1
    print(' x ' if c > 1 else ' = ', end='') # se o valor for maior que 1 ele vai colocar um x se não um =  
    f*=c 
    c-=1  
print(f)
'''


