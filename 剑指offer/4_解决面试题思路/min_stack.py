"""

题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数。在该栈中，调用
min、push及pop的时间复杂度都是O(1)

要求：栈的push，pop，min操作的时间复杂度都是O(1)

思路：使用一个辅助栈保存最小值

"""


class MyStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        return

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        return None

    def min(self):
        return self.min_stack[-1] if self.min_stack else None
