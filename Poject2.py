import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
from Chanka import knoka

f = knoka()

def znach():
    arrx = []
    for i in range(len(f)):
        x, y, z = map(int, f[i].split())
        arrx.append(x)

    return arrx

arrx = znach()

def znach1():
    arry = []
    for i in range(len(f)):
        x, y, z = map(int, f[i].split())
        arry.append(y)

    return arry

arry = znach1()

def znach2():
    arrz = []
    for i in range(len(f)):
        x, y, z = map(int, f[i].split())
        arrz.append(z)

    return arrz

arrz = znach2()
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

def graff():

    x = [i for i in range(0, 200, 100)]
    y = [i for i in range(0, 200, 100)]

    X, Y = np.meshgrid(x, y)
    Z = []
    for i in x:
        t = []
        for j in y:
            t.append(math.tan(math.sqrt(i * 2 + j * 2)))
        Z.append(t)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap=cm.cool)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('3D contour')

    # 2 Модель

    x_value = arrx
    y_value = arry

    x1 = [100000, 1000000]
    y2 = [min_count, min_count]

    fig, axs = plt.subplots(nrows=1, ncols=2)

    fig.suptitle('2D Модель')

    axs[0].plot(x_value, y_value, c='blue')
    axs[1].plot(x1, y2, c='red')

    return plt.show()

print(graff())






