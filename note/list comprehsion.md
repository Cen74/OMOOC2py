

列表推导式


- slice 

- 寻找素数


- 压缩矩阵

>>> matrix =[[0,1,2],[3,4,5],[6,7,8]]
>>> [i for row in matrix for i in row]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> [i for i in row for row in matrix]
[6, 6, 6, 7, 7, 7, 8, 8, 8]