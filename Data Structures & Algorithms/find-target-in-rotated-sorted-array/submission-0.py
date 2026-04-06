class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l<=r:

            mid = l + (r-l) // 2
            # mid is part of left sorted subarray

            if target == nums[mid]:
                return mid
            if target == nums[r]:
                return r
            if target == nums[l]:
                return l

            if nums[mid] > nums[r]:
                # if target is between l and mid
                if target < nums[mid] and target > nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            # mid is part of right sorted subarray
            elif nums[mid] < nums[r]:
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # mid is equal to nums[r]
            else:
                r -= 1

        return -1

                



