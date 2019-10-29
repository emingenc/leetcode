"""
https://leetcode.com/problems/reverse-vowels-of-a-string/

345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


def solution(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    arr = [char for char in s]
    i = 0
    j = len(arr)-1

    while i < j:
        while i < j and arr[i].lower() not in vowels:
            i += 1
        while i < j and arr[j].lower() not in vowels:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return ''.join(arr)


str = solution("leetcode")
print(str)
