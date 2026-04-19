vowel = ['a' , 'e' , 'i' , 'o' , 'u']

s = input()

count = 0
for i in s:
    for j in vowel:
        if j in vowel:
            if i == j :
                count = count +1

print ('Total:' ,count)
