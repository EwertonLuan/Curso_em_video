total = 0
soma = 0

while True:
    n = int(input('Digite um numero ou 999 para parar: '))
    if n == 999:
        break
    else:
        total += 1
        soma += n
print(f'Foram digitados {total} e a soma de todos ele é de {soma}')
