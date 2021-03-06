# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.
#
# Example 1:
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
# Note:
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odds = [num for num in A if num % 2 == 1]
        evens = [num for num in A if num % 2 == 0]
        solution = []
        i = 0
        while i < len(A):
            if i % 2 == 0:
                solution.append(evens.pop())
            else:
                solution.append(odds.pop())
            i += 1
        return solution
s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))
