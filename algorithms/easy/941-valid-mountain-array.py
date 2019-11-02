class Solution:

    def validMountainArray(self, A: List[int]) -> bool:
        if A is None or len(A) < 3:
            return False

        i = 0
        while i + 1 < len(A) and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == len(A) - 1:
            return False

        while i + 1 < len(A) and A[i] > A[i+1]:
            i += 1

        if i != len(A) - 1:
            return False

        return True
