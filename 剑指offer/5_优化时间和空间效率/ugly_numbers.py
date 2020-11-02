"""
面试题34 丑数

要求：只含有2、3、5因子的数是丑数，求第1500个丑数

思路: 按顺序保存已知的丑数，下一个是已知丑数中某三个数乘以2，3，5中的最小值

题目描述：
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

解题方法
第一感觉肯定是把每个数字逐个遍历判断是否是丑数的方式，这样的话效率不高。

比较巧妙的方式是使用空间换时间。我们使用一个数组保存每个丑数，然后生成下一个丑数。

使用了3个指针，分别指向最后一个进行×2，×3，×5操作后会大于当前最大的丑数的位置。
那么需要找到下一个丑数的时候，一定会是这三个指针指向的丑数进行对应操作的结果之一。
因此，每次都更新三个指针指向下一次操作就会变成最大值的位置。就能一直生成下一丑数。

"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        nextNum = 1
        while nextNum < index:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)
            if res[t2] * 2 <= minNum:
                t2 += 1
            if res[t3] * 3 <= minNum:
                t3 += 1
            if res[t5] * 5 <= minNum:
                t5 += 1
            nextNum += 1
        return res[nextNum - 1]
