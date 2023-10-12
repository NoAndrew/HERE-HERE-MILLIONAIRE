from Chanka import knoka

f = knoka()

def znach():
    arrx = []
    for i in range(len(f)):
        x, y, z = map(int, f[i].split())
        arrx.append(x)

    return arrx

def znach1():
    arry = []
    for i in range(len(f)):
        x, y, z = map(int, f[i].split())
        arry.append(y)

    return arry


def znach2():
    arrz = []
    for i in range(len(f)):
        x, y, z = map(int, f[i].split())
        arrz.append(z)

    return arrz

arry = znach1()

def min1():
    min2 = 999999999999
    count = 0
    for j in range(len(f)):
        if min2 > arry[j]:
            count = j
            min2 = arry[j]
    kop = arry[count]

    return kop

min_count = min1() * 0.5







