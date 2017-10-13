__author__ = 'projectx'


class Node(object):
    def __init__(self, init_data):
        # 节点存储的数据
        self.data = init_data
        # 下一节点的引用，引用为None表示没有下一节点
        self.next = None

    def get_data(self):
        """
        获取当前节点的数据

        :return:
        """
        return self.data

    def set_data(self, new_data):
        """
        设置当前节点的数据

        :param new_data:
        :return:
        """
        self.data = new_data

    def get_next(self):
        """
        获取当前节点的下一节点的引用

        :return:
        """
        return self.next

    def set_next(self, new_next):
        """
        设置当前节点的下一节点的引用

        :param new_next:
        :return:
        """
        self.next = new_next


class UnOrderedList(object):
    def __init__(self):
        # 初始化None表示此时链表的头部不引用任何内容
        self.head = None

    def is_empty(self):
        """
        判断链表是否有节点

        :return: true(有节点) or false(没有节点)
        """
        return self.head is None

    def add(self, item):
        # Step0:创建一个新节点并将新项作为数据
        new_node = Node(item)
        # Step1:更改新节点的下一个引用以引用旧链表的第一个节点
        new_node.set_next(self.head)
        # Step2:重新设置链表的头以引用新节点
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            # 当要删除的项目恰好是链表中的第一个项，
            # 这时候previous是None，需要修改head以引用current之后的节点
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


if __name__ == '__main__':
    linked_list = UnOrderedList()
    linked_list.add(78)
    linked_list.add(100)
    linked_list.add(12)
    linked_list.add(22)
    linked_list.add(45)

    print(linked_list.is_empty())
    print(linked_list.size())
    print(linked_list.search(199))
    linked_list.remove(100)

    # if linked_list.head:
    #     current = linked_list.head
    #     while current:
    #         print(current.data)
    #         current = current.get_next()
