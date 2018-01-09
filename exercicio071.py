
a_50 = 0
b_20 = 0
c_10 = 0
d_1 = 0
while True:
    sacar = int(input('Quanto vc deseja sacar: '))
    while sacar % 50 == 0:
        sacar = sacar - 50
        a_50 += 1
        print(sacar)

    print(a_50)
    break

