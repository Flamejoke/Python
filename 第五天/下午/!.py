#泡泡排序法
#第一回合結束，最大的在後面
#因為他跟每個人都比較過

list = [4, 2, 3, 5, 1]
#兩兩座比較  大的排到右邊

第一回合
  2 4 3 5 1 #4 >2所以會換位子(最大的要在最右邊)
  2 3 4 5 1 #4 > 3 ->換位子
  2 3 4 5 1 #4 < 5 ->沒有動

  2 3 4 1 5



import time
t1 = time.time()

list1 = [4, 1, 2, 1, 7, 2, 10, 3]
n = len(list1) # 8
for j in range(n-1):
    # 一個回合，需要n-1個回合
    for i in range(n-1): # i = 0-7
        if list1[i] > list1[i+1]: # 左邊大於右邊
            # 交換
            # Python特有的寫法：list1[i],
            t = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = t

print(list1)

t2 = time.time()
print(t)
