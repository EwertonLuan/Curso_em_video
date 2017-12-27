
from datetime import date
nasci = int(input('Digite o seu ano de nascimento: '))
dat = date.today().year - nasci

print(dat)
if dat <= 17:
    print('Voce ainda vai se alistar daqui a {} ano(s)'.format(18 - dat))
elif 18 <= dat < 19:
    print('Você tem que se alistar esse ano')
else:
    print('Você já passou da data de alistamento a {} ano(s)'.format(dat - 18))
