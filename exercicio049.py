print('{:=^40}'.format('Tabuada'))

numero = int(input('Escolha um numero: '))

for i in range(1, 11):
    mult = numero * i
    print('{} x {} = {}'.format(numero, i, mult))
