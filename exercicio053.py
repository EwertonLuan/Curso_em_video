print('{:=^60}\n'.format('Descubra se a frase é uum palíndromo'))
frase = str(input('Frase: ')).strip().replace(' ', '').upper()  # espaços desnecessarios
revera = ''                                                     # recbe uma frase depois remove os espaços com replace
c = 1                                                           # em seguida passa a frase para maiusculo e remove os

for i in frase:
    revera += frase[-c]
    c += 1
if frase == revera:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')

# Outra resolução
'''frase = str(input('Frase: ')).strip().upper()
separa = frase.split()  #Separa as frases em uma lista
junta = ''.join(separa)  #Remove os espaços do meio da frase frase
reverso = junta[::-1]    # Você pode fatiar a frase ou usar um for deixando reverso = ''

#for letra in range(len(junta)-1, -1, -1): #pega o tamanho da frase com o len, com -1 vai ate e -1 começa pelo ultimo
    #reverso += junta[letra]

if junta == reverso:
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
'''