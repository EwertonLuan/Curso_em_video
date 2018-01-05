primeiro = int(input('O primeiro termo da sua pa:'))
ra = int(input('A razão da sua PA: '))
f = primeiro
c = 1

while c <= 10:
    print(f, end='')
    print(' -> ' if c < 10 else ' -> FIM ', end='')
    f += ra
    c += 1
