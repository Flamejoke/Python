i = 0
while i <100:
    i = i +1
    if i %10 == 0:
        break

print(i)
#i從0一直加到100，當i除10的榆樹等於0，便強制停止while迴圈。
#然後印出i的數值

for j in range(1, 100+1):
    if  j % 2 == 0:
        continue
    print(j,"is odd.")
#j產生1~100的數列，當j除以2餘數為0(偶數),重新執行迴圈,continue以下的程式碼不會被執行。
