primei = maior = menor = total = quantidade = 0

while True:
    while True:
        n = input('Digite um numero ou S para resultados: ').upper().strip()
        if n == 'S':
            break
        else:
            n = int(n)
            primei += 1
            if primei == 1:
                maior = n
            elif n > maior:
                maior = n
            if primei == 1:
                menor = n
            elif menor > n:
                menor = n
            total += n
        quantidade += 1
    media = total / quantidade
    print('A media de todos os numeros é {:.2f} o maior numero digitado foi {} é o menor {} '.format(media, maior,
                                                                                                     menor))
    maior = menor = 0
    repete = str(input('Deseja continuar S/N: ')).strip().upper()
    if repete == 'n':
        break
