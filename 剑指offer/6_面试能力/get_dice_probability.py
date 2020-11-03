"""
面试题43 n个骰子的点数

要求：求出n个骰子朝上一面之和s所有可能值出现的概率

思路：n出现的可能是前面n-1到n-6出现可能的和，设置两个数组，分别保存每一轮

下面思路可能更容易理解。
n个骰子，一共有6**n种情况
n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
可以看作是从前(n-1)个骰子投完之后的状态转移过来。
其中F（N,S）表示投第N个骰子时，点数和为S的次数

原文链接：https://blog.csdn.net/qq_24243877/article/details/104560944


现在变量有：骰子个数，点数和。当有c个骰子，点数和为k时，出现次数记为dp(c, k)。那与c-1各骰子阶段之间的关系是怎样的？

当我有c-1个骰子时，再增加一个骰子，这个骰子的点数只可能为1、2、3、4、5或6，则有：

(c-1, k-1)：第c个骰子投了点数1

(c-1, k-2)：第c个骰子投了点数2

……

(c-1, k-6)：第c个骰子投了点数6

在c-1个骰子的基础上，再增加一个骰子出现点数和为k的结果只有这6种情况，所以：

dp(c, k) = dp(c-1, k-1) + dp(c-1, k-2) + dp(c-1, k-3) + dp(c-1, k-4) + dp(c-1, k-5) + dp(c-1, k-6)
（注意当k<6的处理越界问题）

有一个骰子：

dp(1, 1) = dp(1, 2) = dp(1, 3) = dp(1, 4) = dp(1, 5) = dp(1, 6) =1

因此状态转移方程为：

dp(c)(k) = sum(dp(c-1)(k-m))(1<=m<=g and m<k)

https://www.jianshu.com/p/2ea2c2de6952

"""


def get_ans(n):
    dp = [[0 for _ in range(6*n+1)] for _ in range(n+1)]
    for i in range(1, 7):
        dp[1][i] = 1

    for i in range(2, n+1):
        for j in range(i, i*6+1):
            for k in range(1, 7):
                if j >= k+1:
                    dp[i][j] += dp[i-1][j-k]
    res = []
    for i in range(n, n*6+1):
        res.append(dp[n][i]*1.0/6**n)
    return res
