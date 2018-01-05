primeiro = int(input('Digite o Primeiro termo: '))
ra = int(input('Digite a razão: '))
f = primeiro
total = 0
mais = 10
cont = 1

while mais != 0:
    total += mais
    while cont <= total:
        print(f, end=' ')
        f += ra
        cont += 1
    mais = int(input('\nDigite a quantidade de termos que deseja exibir ou 0 para sair: '))
print('Foram digitados {} termos'.format(total))
