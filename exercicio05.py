print('\033[1;31m#\033[m' * 70
      + '\nQuantos baldes de tinta vao ser necessarios para pintar a casa?\n'
      + '\033[1;31m#\033[m' * 70)

a = int(input('type the heigth: '))
l = int (input('Type it the width: '))

a2 = (a*l)/2
print('will be needed for to paint the wall {} of the paint buckets'.format(a2))




