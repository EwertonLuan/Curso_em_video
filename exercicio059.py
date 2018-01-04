c = 0

while c == 0:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] sair do programaz\n''')
    escolha = int(input('Escolha uma opção: '))
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    resultado = ''
    if escolha == 4:
        c += 1
    if escolha != 4:
        if escolha == 1:
            resultado = n1 + n2
        elif escolha == 2:
            resultado = n1 * n2
        elif escolha == 3:
            resultado = n1 / n2
    print('O resultado a operação é {:.2f}'.format(resultado))
