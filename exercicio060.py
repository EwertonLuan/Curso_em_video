n = int (input('Digite um numero: '))
n_2 = n
sub = n_2 - 1
c = 0
g = ''
while sub >= 0:
    b = n_2 * sub
    c += b
    sub -= 1
    g += str('{} '.format(n_2))
    n_2 = int(n_2)
    n_2 -= 1
g_pronto = g.strip().replace(' ', 'x')
print('O Valor de {}! e {} = {}'.format(n, g_pronto,c))

