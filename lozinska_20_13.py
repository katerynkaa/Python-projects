'''Нехай ми маємо послідовність точок (x0, y0), (x1, y1), …, (xn, yn). При
цьому, x0 < x1 < … < xn. Будемо вважати, що точки yi є значеннями деякої
функції f у точках xi. Інтерполяцією називається побудова функції f у всіх
точках на проміжку [x0, xn].
Одним із способів інтерполяції є застосування інтерполяційного поліному
Лагранжа, який будується за формулою:

Виконати наближення інтерполяційним поліномом Лагранжа функції sin(x)
на відрізку [0, 2π] у (n+1) точці, де n = 2k
, k = 2, 3, 4, … (скласти функцію для
обчислення PL(x)) Використати масиви numpy.
Зобразити на графіках функції sin(x) та PL(x). Зберегти відео (виконати
анімацію) для різних значень k'''

import numpy as np
import matplotlib.pyplot as plt
from math import *
from matplotlib import animation
import matplotlib; matplotlib.use("TkAgg")


def fun(x, yy):
    '''Повертає значення функції f для всіх точок з x
    '''
    try:
        y = sin(x)
        yy += y
    except Exception as e:
        print('Exception handling', e)
        n = x.size
        y = np.zeros(n)
        for i in range(n):
            y[i] = sin(x[i])
            yy += y[i]
    return y


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1; p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1; p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z

k = int(input('кількість точок:'))
n = 2**k

xx = np.linspace(0, 2*pi, 100000)
yy = np.ones(xx.size)

x = np.array([i for i in range(1, n)])
ynew=[lagranz(x,yy,i) for i in x]

s = fun(xx, yy)
plt.plot(xx, s, 'r')
plt.plot(xx,ynew, 'o')

plt.show()

