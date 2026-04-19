# imprort sys :引用外部函式
'''
import sys
print(dir(sys))
'''
'''
import math
print(dir(math))
'''
'''
import time
print(dir(time))
'''
#例題練習
import math

#start
Pi = math.pi

r = float(input())
circumference = 2*r*Pi
area = r*r*Pi
'''
print(round(r,2)) '''#round(數字, 保留小數位數)
#r是半徑, print(round(r, 2))只會輸出半徑

print(round(circumference, 2))
print(round(area, 2))






