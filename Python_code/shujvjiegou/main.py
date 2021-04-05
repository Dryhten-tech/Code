class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    class SingleLinkedList(object):
        def __init__(self):
            """
            :Desc
                单链表初始化
            """
            self.head = None
            self.tail = None
        def empty(self):
            """
            :Desc
                判断单链表是否为空
            :return:
                如果单链表为空，返回True，否则返回False
            """
            return self.head is None

        def length(self):
            """
            :Desc
                获取单链表长度
            :return:
                返回单链表长度
            """
            size = 0
            cur = self.head
            while cur != None:
                size += 1
                cur = cur.next
            return size

        def prepend(self, val):
            """
            头插入法
            :param val:待插入的关键字
            """
            newNode = Node(val)
            if self.head is None:
                self.head = newNode
                self.tail = self.head
            else:
                newNode.next = self.head
                self.head = newNode

        def insert(self, index, value):
            """
            :Desc
                在链表的中间位置插入新节点
            :param index:在下标值index处插入元素，index从0开始
            :param value: 新节点的数据域
            """
            cur = self.head
            for i in range(index - 1):
                cur = cur.next

            temp = cur.next
            newNode = Node(value)
            newNode.next = temp
            cur.next = newNode

        def append(self, val):
            """
            尾插入法
            :param val:待插入的数据元素
            """
            newNode = Node(val)
            if self.empty():
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                self.tail = newNode

        def del_first(self):
            """
            :Desc
                删除头节点
            """
            if self.empty():
                raise IndexError("链表为空")
            if self.length() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        def delete(self, index):
            """
            :Desc
                删除任意位置的节点
            :param index:   删除下标为index的节点
            """
            if self.empty():
                raise IndexError("链表为空")
            if index < 0 or index >= self.lenth():
                raise IndexError("Index在范围之外")

        def def_tail(self):
            """
            Desc
                删除尾节点
            """
            if self.empty():
                raise IndexError("链表为空")
            if self.length() == 1:
                self.head = None
                self.tail = None
            else:
                pre = self.head
