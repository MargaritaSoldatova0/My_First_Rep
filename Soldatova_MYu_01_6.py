'''
1.Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива;
максимальное значение среди элементов второй строки массива. Вывести полученные значения.
2.Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями.
Вывести оба массива.
3.Дана целая квадратная матрица n-го порядка.Определить, является ли она магическим квадратом, т. е. такой матрицей,
в которой суммы элементов во всех строках и столбцах одинаковы.
4.Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
'''
'''
#Задание1
from random import randint
n = 3
arr = list()
for i in range(n):
  brr = list()
  for i in range(n):
    brr.append(randint(0,100))
  arr.append(brr)
print(arr)
max1 = max(arr[0][2],arr[1][2],arr[2][2])
max2 = max(arr[1][0],arr[1][1],arr[1][2])
print(max1,max2)
'''
'''
#Задание2
m = int(input())
n = int(input())
arr = []
print()

for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)
print()

for i in range(m):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()

for i in range(m):
    for j in range(n):
        if arr[i][j] > 0:
            arr[i][j] = 1
        if arr[i][j] < 0:
            arr[i][j] = 0

print()
for i in range(m):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()
'''
'''
#Задание3
    n = int(input())
arr = []
print()

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)

print()
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '  ')
    print()

sum_arr = sum(arr[0])
magic_square = True
col_sum = sum(arr[j])

for i in range(n):
    if sum(arr[i]) != sum_arr:
        magic_square = False
        break

for j in range(n):
    if col_sum != sum_arr:
        magic_square = False
        break

if magic_square:
    print("Это магический квадрат")
else:
    print("Это не магический квадрат")
'''
#Задание4
n = int(input())
arr = []
print()

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    arr.append(a)

print()
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = '  ')
    print()

arr_symmetric = True
for i in range(n):
    for j in range(i, n):
        if arr[i][j] != arr[j][i]:
            arr_symmetric = False
            break

if arr_symmetric:
    print("Матрица явяется симметричной")
else:
    print("Матрица является не симметричной")