class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_cost = [0] * len(cost)

        if len(cost)==1:
            return cost[0]
        

        for k in range(2, len(cost)):
            min_cost[k] = min(min_cost[k-1]+cost[k-1], min_cost[k-2]+cost[k-2])

        return min(min_cost[-1]+cost[-1], min_cost[-2]+cost[-2])
        