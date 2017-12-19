from time import sleep

print('\033[1;34m-=-\033[m' * 20,
      '\n\033[35;1mPrograma que realiza soma de dois numeros\033[m\n' + '\033[1;34m-=-\033[m' * 20)

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
soma = n1 + n2
print('\033[1;35;40mCARREGANDO...\033[m')
sleep(1)
print('\033[4;33m*-*\033[m' * 10
      + '\nA soma de \033[1;33m{}\033[m e \033[1;36m{}\033[m equivale a \033[1;31m{}\33[m\n'.format(n1, n2, soma)
      + '\033[4;33m*-*\033[m' * 10)
