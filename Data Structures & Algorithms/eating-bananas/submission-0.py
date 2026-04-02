class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = max(piles)
        L = 1
        R = max(piles)-1
        while L<=R:
            mid = (L+R)//2
            hours = 0
            for pile in piles:
                hours += pile//mid + (1 if pile % mid >0 else 0)
            if hours <= h:
                min_val = min(min_val,mid)
                R = mid - 1
            else:
                L = mid + 1


        return min_val 





        