
primei = 0
maior = 0
menor = 0
total = 0
quantidade = 0

repete = 0
while repete == 0:
    c = 0
    while c == 0:
        n = int (input('Digite um numero ou 0 para resultados: '))
        if n == 0:
            c += 1
        else:
            primei +=1
            if primei == 1:
                maior = n
            elif n > maior:
                maior = n
            elif primei == 1:
                menor = n
            elif n < menor:
                menor = n


        total += n
        quantidade += 1
    media = total / quantidade
    print('A media de todos os numeros é {:.2f} o maior numero digitado foi {} é o menor {} '.format(media, maior,menor))

    repete = int(input('realizar novamente 0 ou 1 para sair: '))



    #f = str(input('Voce deseja continuar S/N').upper())




