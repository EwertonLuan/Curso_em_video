vezes = int(input('Quantos numeros da seuquência de fibonacci: '))
a = 0
b = 1
i = 3 # comeeça a contagem em 3 pq já recebeu 'a', 'b' 

print('{} {}'.format(a, b), end=' ')
while i <= vezes:
     c = a + b
     print('{} '.format(c), end=' ')
     b = c
     a = b
     i+=1


