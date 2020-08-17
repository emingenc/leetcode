"""
9. Fizz Buzz

Description
Given number n. Print number from 1 to n. But:

- when number is divided by 3, print "fizz".
- when number is divided by 5, print "buzz".
- when number is divided by both 3 and 5, print "fizz buzz".
- when number can't be divided by either 3 or 5, print the number itself.

Example

If n = 15, you should return:
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]

If n = 10, you should return:
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz"
]

Challenge
Can you do it with only one if statement?

"""


def fizzBuzz(self, n):
    output = [str(i + 1) for i in range(n)]
    i = 1
    while i*3 - 1 <= n-1:
        output[i*3 - 1] = 'fizz'
        i += 1
    i = 1
    while i*5 - 1 <= n-1:
        output[i*5 - 1] = 'buzz'
        i += 1
    i = 1
    while i*15 - 1 <= n-1:
        output[i*15 - 1] = 'fizz buzz'
        i += 1
    return output
