
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')

# ou simplificando
print('')
for cont in range(2, 51, 2):# dessa forma ele diminui a quantidade de laços e faz saltos de 2 em 2 pegando apenas os
    print(cont, end=' ')             # numeros pares