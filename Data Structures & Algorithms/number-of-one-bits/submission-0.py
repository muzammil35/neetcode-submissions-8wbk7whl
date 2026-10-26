class Solution:
    def hammingWeight(self, n: int) -> int:
        count = lambda x: x.count('1')
        return count((str(bin(n))))