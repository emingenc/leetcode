"""
https://www.geeksforgeeks.org/find-maximum-number-possible-by-doing-at-most-k-swaps/


Find Maximum number possible by doing at-most K swaps

Given a positive integer, find maximum integer possible
by doing at-most K swap operations on its digits.

Input: M = 254, K = 1
Output: 524
Swap 5 with 2 so number becomes 524

Input: M = 254, K = 2
Output: 542
Swap 5 with 2 so number becomes 524
Swap 4 with 2 so number becomes 542

Input: M = 68543, K = 1
Output: 86543
Swap 8 with 6 so number becomes 86543

Input: M = 7599, K = 2
Output: 9975
Swap 9 with 5 so number becomes 7995
Swap 9 with 7 so number becomes 9975

Input: M = 76543, K = 1
Output: 76543
Explanation: No swap is required.

Input: M = 129814999, K = 4
Output: 999984211
Swap 9 with 1 so number becomes 929814991
Swap 9 with 2 so number becomes 999814291
Swap 9 with 8 so number becomes 999914281
Swap 1 with 8 so number becomes 999984211

Algorithm:

1. Create a global variable which will store the maximum string or number.
2. Define a recursive function that takes the string as number and value of k
3. Run a nested loop, the outer loop from 0 to length of string -1
and inner loop from i+1 to end of string.
4. Swap the ith and jth character and check if the string is now maximum
and update the maximum string.
5. Call the function recursively with parameters: string and k-1.
6. Now again swap back the ith and jth character.

Time Complexity: O(n^k).
For every recursive call n recursive calls is generated until the value of k is 0. So total recursive calls are O((n)^k).
Space Complexity: O(n).
The space required to store the output string.

"""


def swap(string, i, j):
    """
    utility function to swap two characters of a string
    """
    str_list = list(string)
    str_list[i], str_list[j] = str_list[j], str_list[i]
    return ''.join(str_list)
    # return (string[:i] + string[j] +
    #        string[i + 1:j] +
    #        string[i] + string[j + 1:])


def findMaximumNum(string, k, maxnum):
    if k == 0:
        return maxnum
    maxnum = max(maxnum, int(string))
    n = len(string)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if string[i] < string[j]:
                string = swap(string, i, j)
                maxnum = findMaximumNum(string, k - 1, maxnum)
                string = swap(string, i, j)
    return maxnum


# Driver Code
if __name__ == "__main__":
    string = "129814999"
    k = 4
    maxm = findMaximumNum(string, k, int(string))
    print(maxm)
