#Домашнее задание

'''

1.Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2).
Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный.
Вычисления оформить в виде процедуры.
2.Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет собой палиндром,
т. е. читается одинаково слева направо и справа налево.

'''
'''
#Задание1
import math
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
z1 = int(input()) 
z2 = int(input())
def a(x,y):
    b = math.degrees(math.atan(abs(y/x)))
    return b
def c(i,j,k):
    d = min(i,j,k)
    if d ==i:
        print(x1,x2)
    elif d == j:
        print(y1,y2)
    elif d == k:
        print(z1,z2)
c(a(x1,x2),a(y1,y2),a(z1,z2))
'''
#Задание2
n = int(input())
def a(b):
    c = 0
    for i in range(2,b//2+1):
        if (b % i == 0):
            c = c+1
    if (c <= 0):
        return 1
    else:
        return 0
def d(e):
    return e == e[::-1]
def c(n):
    for i in range(2,n):
        if a(i) == 1:
            s = str(bin(i))
            s = s[2:]
            if d(s) == True:
                print(i)
c(n)
