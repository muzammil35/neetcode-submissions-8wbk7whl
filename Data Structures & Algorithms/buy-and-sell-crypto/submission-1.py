class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        cur_max = 0
        while L < len(prices)-1 and R <= len(prices)-1:
            if prices[R] < prices[L]:
                L = R
                R = L + 1
            elif prices[L] < prices[R]:
                cur_max = max(cur_max, prices[R]-prices[L])
                R +=1
            else:
                R+=1
        return cur_max