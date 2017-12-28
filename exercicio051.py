print('{:#^50}'.format('\033[1;34;41mCauculando uma PA\033[m'))

pri_ter = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
pa = pri_ter
print(pri_ter)
for i in range (1,10):
    pa =  pa + razao
    print(pa)

