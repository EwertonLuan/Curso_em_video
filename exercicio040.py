nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print('Aluno ficou com media {}, sendo \033[1;31mREPROVADO\033[m'.format(media))
elif media <= 6.9:
    print('Aluno tirou uma media de {} ficando de \33[1;32mRECUPERAÇÃO\033[M'.format(media))
else:
    print('O aluno tirou uma media de {} sendo \033[1;34mAPROVADO\033[m'.format(media))