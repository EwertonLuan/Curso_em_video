print('\033[1;34m<^>\033[m' * 30
      + '\n \n\033[4;1;32mCaucule a media da nota das provas\033[m\n')
print('Legenda:\n'+'\033[1;44m  \033[m Nota Azul\n'+'\033[1;41m  \033[m Nota vermelha\n')
print('\033[1;34m<^>\033[m' * 30 + '\n')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

print('\033[1;30m~^~\033[m' * 30+'\n')
print('O aluno tirou na primeira prova {} e {} na segunda prova, ficou com media de {} no total\n'.format(
    '\033[1;34m' + str(n1) + '\033[m' if n1 >= 5 else '\033[1;31m' + str(n1) + '\033[m',
    '\033[1;34m' + str(n2) + '\033[m' if n2 >= 5 else '\033[1;31m' + str(n2) + '\033[m',
    '\033[1;34m' + str(m) + '\033[m' if m >= 5 else '\033[1;31m' + str(m) + '\033[m'))
print('\033[1;30m~^~\033[m' * 30)
