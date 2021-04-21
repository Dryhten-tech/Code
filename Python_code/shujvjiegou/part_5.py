class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def length(self):
        size = 0
        cur = self.head
        while cur is not None:
            size += 1
            cur = cur.next
        return size

    def prepend(self, val):
        newNode = Node(val)
        if self.empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def del_first(self):
        if self.empty():
            raise IndexError('Index非法')
        self.head.next.prev = None
        self.head.prev = None

    def append(self, val):
        newNode = Node(val)
        if self.empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def traversal(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end='')
            cur = cur.next
        print()

    def under_traversal(self):
        cur = self.tail
        while cur is not None:
            print(cur.val, end='')
            cur = cur.prev
        print()

    def insert(self, index, val):
        if index >= self.length() or index < 0:
            raise IndexError('Index非法')
        cur = self.head
        newNode = Node(val)
        idx = 0
        if self.empty():
            self.head = newNode
            self.tail = newNode
        else:
            while idx < index:
                cur = cur.next
                idx += 1

            cur.prev.next = newNode
            cur.prev = newNode
            newNode.next = cur
            newNode.prev = cur.prev

    def delete(self, index):
        cur = self.head
        for i in range(index - 1):
            pre = cur.next
        delNode = cur.next
        nextNode = delNode.next
        pre.next = nextNode

    def del_last(self):
        if self.empty():
            raise IndexError('Index非法')
        self.tail = self.tail.prev
        self.tail.next = None

    def find(self, key):
        cur = self.head
        while cur is not None:
            if key == cur.val:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    print('程序开始执行')
    print()
    print('开始实现任务一')
    print('开始初始化双链表')
    double_list = DoubleLinkedList()
    for i in range(1, 10, 1):
        double_list.append(i)
    print('输出初始化完成的双链表')
    double_list.traversal()
    print('双链表初始化已完成')
    print()
    print('现在开始进入功能实现阶段')
    # 以下为功能实现
    print('现在执行表头插入语句')
    print('功能为:在双链表的表头插入数字7')
    double_list.prepend(7)  # 在双链表的表头插入数字7
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('现在执行中间插入语句')
    print('功能为:在index为5的地方插入一个数字8')
    double_list.insert(5, 8)  # 在index为5的地方插入一个数字8
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('现在执行表尾插入语句')
    print('功能为:在双链表的表尾插入数字9')
    double_list.append(9)  # 在双链表的表尾插入数字9
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('现在执行表头删除语句')
    print('功能为:删除双链表的表头')
    double_list.del_first()  # 删除双链表的表头
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('现在执行表中元素删除语句')
    print('功能为:删除双链表的index为5的元素')
    double_list.delete(5)  # 删除双链表的index为5的元素
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('现在执行表尾删除语句')
    print('功能为:删除双链表的表尾')
    double_list.del_last()  # 删除双链表的表尾
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('现在执行查找表中指定值的节点语句')
    print('功能为:查找值为8的index')
    double_list.find(8)  # 查找值为8的index
    print('功能已执行，现输出执行功能后的双链表')
    double_list.traversal()
    print('双链表输出已完成')
    print()
    print('任务一已全部完成，开始执行任务二')
    print('开始初始化双链表')
    double_list = DoubleLinkedList()
    for i in range(1, 10, 1):
        double_list.append(i)
    print('输出初始化完成的双链表')
    double_list.traversal()
    print('双链表初始化已完成')
    print()
    print('现在开始进入功能实现阶段')
    print('现在执行逆序输出链表中每一个元素的值')
    double_list.under_traversal()
    print('任务二已全部完成')
    print()
    print('所有任务已全部完成')
    print('功能已全部实现，程序退出')
