class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map_ = {}
        for i,el in enumerate(nums):
            map_[el] = i
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -1*(nums[i] + nums[j]) in map_ and map_[-1*(nums[i] + nums[j])] != i and map_[-1*(nums[i] + nums[j])] != j:
                    candidate = [nums[i], nums[j], -1*(nums[i]+nums[j])]
                    
                    if sorted(candidate) not in ret:
                        ret.append(sorted(candidate))
        return ret

            
