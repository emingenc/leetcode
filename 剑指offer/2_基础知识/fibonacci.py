"""
https://github.com/JushuangQiao/Python-Offer/tree/master/second/fourth

面试题9 斐波那契数列
思路：用生成器


"""


def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield b
        a, b = b, a + b
