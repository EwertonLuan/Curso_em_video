n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0


while escolha != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa\n''')

    escolha = int(input('Escolha uma opção: '))
    if escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 1:
        resultado = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print(' {} x {} = {}'.format(n1, n2, resultado))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o meior numero é {}'.format(n1, n2, maior))
    elif escolha == 5:
        print('Saindo do programa')
    else:
        print('\n\033[1;31mOpção invalida tente novamente!\033[m\n')
