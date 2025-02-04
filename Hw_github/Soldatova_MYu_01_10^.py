'''
1.Создать объект pandas Series из листа, объекта NumPy, и словаря
2.Получить не пересекающиеся элементы в двух объектах Series
3.Узнать частоту уникальных элементов объекта Series (гистограмма)
4.Объединить два объекта Series вертикально и горизонтально
5.Найти разность между объектом Series и смещением объекта Series на n
'''
'''
#Задание 1
import numpy as np
import pandas as pd
x_l = list('абв')
y_a = np.arange(3)
c_d = dict(zip(x_l, y_a))
a = pd.Series(x_l)
b = pd.Series(y_a)
c = pd.Series(c_d) 
print(a)
print(b)
print(c)
'''
'''
#Задание 2
import pandas as pd
import numpy as np
a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([4, 5, 6, 7, 8])
c=pd.Series(np.setxor1d(a, b))
print(c)
'''
'''
#Задание 3
import numpy as np
import pandas as pd
l = np.random.randint(1, 5, 10)
print(*l)
a = pd.Series(l)
b = a.value_counts()
print(b)
'''
'''
#задание4
import pandas as pd
a = pd.Series(range(5))
b = pd.Series([6,7,8,9,10])
x = pd.concat([a, b], axis=1)
y = pd.concat([a, b])
 
print(y)
print(x)
'''
#задание5
import pandas as pd
n = int(input('введите n:'))
с = pd.Series([1, 2, 5, 9, 11, 18])
a = с.diff(n)
print(a)