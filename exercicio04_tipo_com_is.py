
print('\033[1;32m=*\033[m' * 20 + '\nDescobrindo o Tipo da variavel\n' + '\033[1;32m=*\033[m' * 20)
n = input('Digite algo: ')
print(type(n))
print('É alhpha numerico ?\n',n.isalnum(),'\nÉ alpha?\n',n.isalpha(),'\nÉ numero?\n',n.isnumeric())