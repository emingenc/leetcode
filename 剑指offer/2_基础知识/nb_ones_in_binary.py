"""
面试题10 二进制中1的个数
要求：求一个整数的二进制表示中，1的个数

思路：二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1

"""


def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret


def num_of_ones(n):
    bin_n = "{0:b}".format(n)
    return sum([1 for i in bin_n if int(i) == 1])
