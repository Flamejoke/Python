#資料結構
#堆疊 stack
'''
stack = []

def push(data):
    stack.append(data)

def pop():
    r = stack.pop
    #紀錄我們拿了什麼元素出來
    return r
    '''
#queue
#start
'''
queue = []

def enqueue(data):
    dequeu.append(data)

def dequeue(data):
    data = queue.pop(0)
    return data
#pop()預設是拿最後面的元素
#有數字,會拿那個索引直

def isFull():
    if len(queue) == MAX_SIZE:
        return True
    else:
        return False


def isEmpty():
    if len (queue) == 0:
        return True
    else : False

def front():
    return queue[0]

def rear():
    return queue[len(queue)-1]
'''
MAX_SIZE = 10
#start
for i in range (11):
    if isFull() == False:
        enqueue(i)
    else:
        print("Queue is full, can't add item.")





















