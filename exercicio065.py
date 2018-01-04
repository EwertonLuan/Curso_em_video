
c = ''
repete = ''
while not 'N' in repete:
    while not 'N' in c:
        primei = 0
        maior = 0
        menor = 0
        total = 0
        quantidade = 0
        n = str(input('Digite um numero ou S(sair) para ver os resultados: ').upper())
        if n == 'S':
            media = total / quantidade
            print('A media de todos os numeros é {:.2f} o maior numero digitado foi {} é o menor {} '.format(media, maior, menor))
            c= n

        else:
            n = int(n)
            primei +=1
            if primei == 1:
                maior = n
            elif n > maior:
                maior = n
            if primei == 1:
                menor = n
            elif n < menor:
                menor = n
            total += n
            quantidade += 1



    f = str(input('Voce deseja continuar S/N').upper())
    if f == 'N':
        repete += f



