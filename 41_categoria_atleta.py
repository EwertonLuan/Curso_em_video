from datetime import date
print('\033[1;32m##\033[m' * 20+'\nPrograma para ver a categoria dos atletas\n'+'\033[1;32m##\033[m'*20)
ida = date.today().year - int(input('Qual a idade do atleta: '))

if ida <= 9:
    print('Atleta esta com {} anos, sua categoria é \033[1;33mMIRIM\033[m'.format(ida))
elif ida <= 14:
    print('Atleta esta com {} anos, sua categoria é \033[1;34mINFANTIL\033[m'.format(ida))
elif ida <= 19:
    print('Atleta esta com {} anos, sua categoria é \033[1;35mJUNIOR\033[m'.format(ida))
elif ida <= 20:
    print('Atleta esta com {} anos, sua categoria é \033[1;36mSENIOR\033[m'.format(ida))
else:
    print('Atleta esta com {} anos, sua categoria é \033[1;31mMASTER\033[m'.format(ida))