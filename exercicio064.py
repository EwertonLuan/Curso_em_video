c = 0
soma = 0
quan = 0

while c != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        c += n
    else:
        soma += n
        quan += 1
print('a soma do {} numeros que foram digitados é de {}'.format(quan,soma))