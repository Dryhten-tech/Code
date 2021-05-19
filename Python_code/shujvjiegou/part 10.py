class SeqQueue(object):
    def __init__(self, max):
        self.max = max
        self.front = 0
        self.rear = 0
        self.data = [None for i in range(self.max)]


class CircleQueue(object):
    def __init__(self, max):
        self.max = max
        self.data = [None for i in range(self.max)]
        self.front = 0
        self.rear = 0

    def empty(self):
        return self.front == self.rear

    def push(self, val):
        if (self.rear + 1) % self.max == self.front:
            raise IndexError("队列已满")
        self.data[self.rear] = val
        self.rear = (self.rear + 1) % self.max

    def peek(self):
        if self.empty():
            raise IndentationError("列表为空")
        cur = self.data[self.front]
        self.front = (self.front + 1) % self.max
        return cur

    def pop(self):
        if self.empty():
            raise IndexError("队列为空")
        return self.data[self.front]


if __name__ == '__main__':
    c = CircleQueue(4)
    c.push(3)
    c.push(5)
    c.push(7)
    print(c.peek())
    c.pop()
    print(c.peek())

# In[3]:


import random

a = random.randint(10, 99)
print(a)
jieguo = 0
for i in range(2, a):
    if a % i == 0:
        jieguo = jieguo + 1
if jieguo > 0:
    print("非素数")
else:
    print("素数")

# In[ ]:


# In[ ]:
