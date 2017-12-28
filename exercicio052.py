c = 0
num = int(input('Digite um numero: '))
for i in range (2,12):
    primo = num % i
    c = c + primo
    print( primo)

if c != 0:
    print(c)
else:
    print('não', c)