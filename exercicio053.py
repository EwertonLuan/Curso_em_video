print('{:=^60}\n'.format('Descubra se a frase é uum palíndromo'))
frase = str(input('Frase: ')).replace(' ', '').upper().strip()
revera = ''
c = 1

for i in frase:
    revera += frase[-c]
    c += 1
if frase == revera:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
