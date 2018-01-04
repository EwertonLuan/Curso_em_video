
a = int(input('Digite um numero: '))
vezes = int(input('Quantos numeros da seuquência de fibonacci: '))
v_d = int(vezes/2)
b = a
c = 1
while c <= v_d:
     print(b,a, end=' ')
     b+= a
     a+=b
     c+=1


