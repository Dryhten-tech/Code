class SeqStack(object):
    def __init__(self, max):
        self.max = max
        self.top = -1
        self.stack = [None for i in range(self.max)]

    def empty(self):
        return self.top is -1

    def push(self, val):
        if self.top == self.max - 1:
            raise IndexError("栈已满")
        else:
            self.top += 1
            self.stack[self.top] = val

    def pop(self):
        if self.empty():
            raise IndexError("栈为空")
        else:
            cur = self.stack[self.top]
            self.top -= 1
            return cur

    def peak(self):
        if self.empty():
            raise IndexError("栈为空")
        else:
            return self.stack[self.top]

    def traversal(self):
        while self.empty() == False:
            print(self.pop())


def w_in():
    k = int(input("请输入想转换的进制："))
    if k == 2 or k == 8 or k == 16:
        return k
    else:
        print("请输入有效进制")
    return w_in()


if __name__ == "__main__":
    s = SeqStack(50)
    in_word = w_in()
    i = int(input("请输入转进制的数："))
    while i >= in_word:
        a = i % in_word
        if a > 9:
            a = chr(64 + (a - 9))
        s.push(a)
        i = i // in_word
    s.push(i)
    s.traversal()
