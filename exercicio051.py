print('{:#^50}'.format('\033[1;34;41mCauculando uma PA\033[m'))

pri_ter = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = pri_ter + (10 - 1) * razao #Calculando o decimo termo de uma pa

for i in range (pri_ter,decimo + razao, razao):
        print(i, end= ' ')

