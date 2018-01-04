primeiro = int(input('Digite o Primeiro termo: '))
ra = int(input('Digite a razão: '))
c = 0
t = 0
while t != 1:
    while c <= 9:
        print(primeiro, end=' ')
        primeiro += ra
        c += 1
    t = int(input('Digite a quantidade de termos que deseja exibir ou 0 para sair: '))
    if t == 0:
        t+=1
    else:
        print(t)
        i = 0
        while i <= t-1:
            print(primeiro, end=' ')
            primeiro += ra
            i += 1
