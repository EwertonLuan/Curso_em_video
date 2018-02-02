a_50 = 0
b_20 = 0
c_10 = 0
d_1 = 0
sacar = int(input('Quanto vc deseja sacar: R$'))
while sacar > 0:
    if sacar >= 50:
        sacar = sacar - 50
        a_50 += 1
    elif sacar >= 20:
        sacar = sacar - 20
        b_20 += 1
    elif sacar >= 10:
        sacar = sacar - 10
        c_10 += 1
    elif sacar >= 1:
        sacar = sacar - 1
        d_1 += 1
    if sacar == 0:
        break


if a_50 > 0:
    print(F'total de celulas de 50 {a_50}')
if b_20 > 0:
    print(f'total de celulas de 20 {b_20}')
if c_10 > 0:
    print(f'total de celulas de 10 {c_10}')
if d_1 > 0:
    print(f'total de celulas de 1 {d_1}')

