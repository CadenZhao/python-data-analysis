# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:28:45 2018

@author: Caden
"""


import numpy as np
#------------------------------------------------------------------------------------------------------------------------------------------
#数组的元素类型可以通过dtype 属性获得
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])
print(c.dtype)

#通过shape属性获取、改变数组形状
print(c.shape)
c.shape=4,3                      #可以用-1代替4或3中的一个，它会自动补全形状
print(c.shape)

#数组的reshape方法可以不改变原数组，但d和a内存你地址相同，改变d会同时改变a
a = np.array([1, 2, 3, 4])
d=a.reshape(2,-1)
"""
d
Out[44]: 
array([[1, 2],
       [3, 4]])

a
Out[45]: array([1, 2, 3, 4])
"""

#array()的dtype参数可以在创建数组时指定元素类型
e=np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.float)
f=np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.complex)
print(e,f)
"""
[[ 1.  2.  3.  4.]
 [ 4.  5.  6.  7.]
 [ 7.  8.  9. 10.]] [[ 1.+0.j  2.+0.j  3.+0.j  4.+0.j]
 
 [ 4.+0.j  5.+0.j  6.+0.j  7.+0.j]
 [ 7.+0.j  8.+0.j  9.+0.j 10.+0.j]]
"""


#------------------------------------------------------------------------------------------------------------------------------------------






