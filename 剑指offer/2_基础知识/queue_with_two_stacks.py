"""
面试题7 用两个栈实现队列

要求：用两个栈实现队列，分别实现入队和出队操作 

思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中

"""


class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else None
