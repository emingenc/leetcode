"""
https://leetcode-cn.com/problems/implement-stack-using-queues/

225. Implement Stack using Queues

Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue,
which means only push to back, peek/pop from front, size,
and is empty operations are valid.
Depending on your language, the queue may not be supported natively.
You may simulate a queue using a list or deque (double-ended queue),
as long as you use only a queue's standard operations.

Follow-up: Can you implement the stack such that each operation
is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time
even if one of those operations may take longer.

 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.


复杂度分析

时间复杂度：入栈操作 O(n)O(n)，其余操作都是 O(1)O(1)。
入栈操作需要将 \textit{queue}_1queue 
1
​	
  中的 nn 个元素出队，并入队 n+1n+1 个元素到 \textit{queue}_2queue 
2
​	
 ，共有 2n+12n+1 次操作，每次出队和入队操作的时间复杂度都是 O(1)O(1)，因此入栈操作的时间复杂度是 O(n)O(n)。
出栈操作对应将 \textit{queue}_1queue 
1
​	
  的前端元素出队，时间复杂度是 O(1)O(1)。
获得栈顶元素操作对应获得 \textit{queue}_1queue 
1
​	
  的前端元素，时间复杂度是 O(1)O(1)。
判断栈是否为空操作只需要判断 \textit{queue}_1queue 
1
​	
  是否为空，时间复杂度是 O(1)O(1)。

空间复杂度：O(n)O(n)，其中 nn 是栈内的元素。需要使用两个队列存储栈内的元素。


"""

import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1
