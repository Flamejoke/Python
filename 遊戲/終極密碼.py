import random
num = random.randint(1, 99)
answer = 0
point = 0
Max = 99
Min = 1
Str = "歡迎來到中及密碼，猜中了報詐，為猜中將獲得點數，請猜數字"
while answer != num :
    answer = eval(input(Str + str(Min) + " to " + str(Max) + ":"))
    if answer > Max or answer < Min:
        print("不在範圍內")
        
    elif answer > num:
        Max = answer - 1
        print(Min,"to",Max)
        point = point + 1
        
    elif answer < num :
        Min = answer + 1
        print(Min, "to", Max)
        point = point + 1
        
    else: 
        print("爆炸了")
        point = point - 1
        go = input("目前累積分數:" + str(point)55 + "是否繼續 Y?:" )
        if go  == "Y" or go ==  "y":
            num = random.randint(1, 99)
            answer = 0
            Min = 1 
            Max = 99
        else :
            print("得分", point)
            
        
    