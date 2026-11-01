class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)

        if n == 1:
            return 1
        if n == 2:
            return 2
        arr[1] = 1
        arr[2] = 2

        for j in range(3, n+1):
            arr[j] = arr[j-1] + arr[j-2]

        return arr[n]
        