import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
from Poject3 import *

arrx = znach()
arry = znach1()
arrz = znach2()


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
