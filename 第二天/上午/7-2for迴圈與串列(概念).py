import sys
#串列為一種可迭代的物件(range,string,list,tuple,set...)

#list串列
name = ['amy' , 'kevin' , 'black' , 'tom' , 'cloud']

for student in name :
    print('Hello,' , student) #for迴圈從name(串列)中取出一個元素(amy,kevin...)，放入student(變數)中進行計算

#字串
for s in 'Hello,world!':
    print(s,end=' ')
    
#sys.stdin:一行字串
i = 'Hello'
for i in sys.stdin:
    print(i,end=' ')

