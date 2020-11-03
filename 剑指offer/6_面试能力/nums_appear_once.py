"""
面试题40 数组中只出现一次的数字

要求：数组中除了两个只出现一次的数字外，其他数字都出现了两遍

思路: 按位异或，在得到的值中找到二进制最后一个1，然后把数组按照该位是0还是1分为两组

"""


def FindNumsAppearOnce(array):
    xor = 0
    for i in array:
        xor ^= i
        print(xor)
    num1, num2 = 0, 0
    mask = 1
    while xor & mask == 0:
        mask <<= 1
    for num in array:
        if num & mask == 0:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


if __name__ == '__main__':
    array = [1, 3, 1, 2, 4, 2]
    print(FindNumsAppearOnce(array))
    print(1 ^= 3)
