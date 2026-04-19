#start

import sys
list1 = [4,3,2,1]

for s in sys.stdin:
    s = s.split() # 被分割後 => 變成串列
    n = len(s)
    if n ==1:
        if s[0] == 1:
            print(len(list1))
        else:
            list1.sort() #排序
            print(len(list1))
            print(list1)
            
