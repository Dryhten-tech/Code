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
        while cur is not None:
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
        if index < 0 or index >= self.length():
            raise IndexError("Index在范围之外")
        if index == 0:
            self.del_first()
        elif index == self.length() - 1:
            self.del_last()
        else:
            pre = self.head
            for i in range(index - 1):
                pre = pre.next
            delNode = pre.next
            next = delNode.next
            pre.next = next

    def del_last(self):
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
            cur = pre.next

            while cur.next is not None:
                pre = cur
                cur = cur.next
            cur = None
            pre.next = None
            self.tail = pre

    def find(self, key):
        """
        :Desc
            在单链表中查找关键字
        :param key: 关键字
        :return:
            查找成功，返回True
            查找失败，返回False
        """
        cur = self.head
        while cur is not None:
            if key == cur.val:
                return True
            cur = cur.next

        return False

    def traversal(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end='')
            cur = cur.next


if __name__ == "__main__":
    single_list = SingleLinkedList()
    print("第一题开始")
    for i in range(1, 10, 1):
        single_list.append(i)
    single_list.traversal()
    print("更新表链")
    single_list.prepend(5)
    print("头部插入一个5")
    single_list.traversal()
    print("更新表链")
    single_list.insert(3, 8)
    print("index为3的地方插入一个8")
    single_list.traversal()
    print("更新表链")
    single_list.append(6)
    print("尾部插入一个6")
    single_list.traversal()
    print("更新表链")
    single_list.del_first()
    print("删除头部")
    single_list.traversal()
    print("更新表链")
    single_list.delete(4)
    print("删除index为4的元素")
    single_list.traversal()
    print("更新表链")
    single_list.del_last()
    print("删除尾部")
    single_list.traversal()
    print("更新表链")
    if single_list.find(5):
        print("找到元素5")
    else:
        print("未找到元素5")
    print("第一题结束")
    print()
    print("第二题开始")
    single_list = SingleLinkedList()
    for i in range(1, 10, 1):
        single_list.append(i)
    single_list.traversal()
    print("更新表链")
    print("插入一个6")
    t = single_list.head
    idx = 0
    while t is not None and not (t.val >= 6):
        t = t.next
        idx += 1
    single_list.insert(idx, 6)
    single_list.traversal()
    print("更新表链")
    print("第二题结束")
    print()
    print("第三题开始")
    single_list = SingleLinkedList()
    for i in range(1, 10, 1):
        single_list.append(i)
        single_list.append(i)
        single_list.append(i)
    single_list.traversal()
    print("更新表链")
    t = single_list.head
    idx = 1
    max_t = 0
    while t is not None:
        if t.val > max_t:
            max_t = t.val
            idx = 1
        elif t.val == max_t:
            idx += 1
        t = t.next
    print(str(idx) + "个")
    print("第三题结束")
