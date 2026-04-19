import sys

def addvalue(a, b):
    c = int(a) + int(b)
    return c

def addstring(a, b):
    c = str(a) + str(b)
    return c

#start
for s in sys.stdin:
    data = s.split()
    
    if data[0] == "1":
        r = addvalue(data[1], data[2])
        
    elif data[0] == "2":
        r = addstring(data[1], data[2])
        
    print(r)


