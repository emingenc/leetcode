"""
面试题5 从尾到头打印单链表

"""


class Node(object):
    def __init__(self) -> None:
        self.next = None


def print_links(links: Node):
    # 方法1：使用栈,可以使用列表模拟
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


def print_link_recursion(links: Node):
    # 方法2：直接递归
    if links:
        print_link_recursion(links.next)
        print(links.val)
