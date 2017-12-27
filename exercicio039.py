
from datetime import date
sexo = str(input('Digite M para sexo masculino e F para sexo feminino: ')).upper()
if sexo == 'F':
    servir = str(input('Mulheres não são obrigas a servir, você deseja continuar S/N: ').upper())
    if servir == 'S':
        sexo = 'M'
nasci = int(input('Digite o seu ano de nascimento: '))
dat = date.today().year - nasci

if sexo == 'M':
    if dat <= 17:
        print('Voce ainda vai se alistar daqui a {} ano(s)'.format(18 - dat))
    elif 18 <= dat < 19:
        print('Você tem que se alistar esse ano')
    else:
        print('Você já passou da data de alistamento a {} ano(s)'.format(dat - 18))
