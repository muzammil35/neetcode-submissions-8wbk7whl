class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        if r == l:
            return nums[0]
        found_min = 1001
        while l<r:
            mid = l + (r-l // 2)

            # if the mid is part of the left sorted subarray
            if nums[mid] > nums[l]:
                found_min = min(found_min, nums[l])
                l = mid + 1
            # mid must be part of the right sorted subarray
            elif nums[mid] < nums[l]:
                found_min = min(found_min, nums[mid])
                r = mid - 1
            
        return found_min
            

        