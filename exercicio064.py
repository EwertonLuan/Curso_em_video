n = 0
soma = 0
quan = 0

while n != 999:
    n = int(input('Digite um numero ou 999 para sair: '))
    if n != 999:
        soma += n
        quan += 1
print('a soma do {} numeros que foram digitados é de {}'.format(quan,soma))