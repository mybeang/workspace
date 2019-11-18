from queue import Queue

"""
Test Data: [0, 1, 2, 3, 4, 5]

********************
case1: no exception for full
input data: 0
current q = deque([0])
input data: 1
current q = deque([0, 1])
input data: 2
current q = deque([0, 1, 2])
input data: 3
Meet raise: Queue is Full [data = 3]
input data: 4
Meet raise: Queue is Full [data = 4]
input data: 5
Meet raise: Queue is Full [data = 5]

********************
case2: FIFO
input data: 0
result = deque([0])
input data: 1
result = deque([0, 1])
input data: 2
result = deque([0, 1, 2])
input data: 3
result = deque([1, 2, 3])
input data: 4
result = deque([2, 3, 4])
input data: 5
result = deque([3, 4, 5])
"""

test_data = [i for i in range(6)]
print("Test Data: {}".format(test_data))

print("")
print("*" * 20)
print("case1: no exception for full")
q = Queue(3)
for i in test_data:
    print("input data: {}".format(i))
    try:
        q.put(i, block=False)
        print("current q = {}".format(q.queue))
    except:
        print("Meet raise: Queue is Full [data = {}]".format(i))

del q

print("")
print("*" * 20)
print("case2: FIFO")
q = Queue(3)
for i in test_data:
    print("input data: {}".format(i))
    if q.full():
        q.get()
        q.put(i, block=False)
    else:
        q.put(i, block=False)
    print("result = {}".format(q.queue))

