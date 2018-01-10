total = 0
soma = 0

while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    total += 1
    soma += n
print('Foram digitados {} e a soma de todos ele é de {}'.format(total,soma))
