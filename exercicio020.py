import random

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de um aluno: ')
a3 = input('Digite o nome de um aluno: ')
a4 = input('Digite o nome de um aluno: ')
lista = [a1,a2,a3,a4]
sorteio = random.shuffle(lista)
print(lista)