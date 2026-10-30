class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        sets.append([])
        for i, num in enumerate(nums):
            set_ = (self.getsubsets(i, [num], nums, len(nums), []))
            sets += set_
        return sets

    def getsubsets(self, i, cur, nums, maxlen, record):
        if cur not in record:
            record.append(cur)
        if len(cur) > maxlen:
            return
        for j,num in enumerate(nums):
            if num not in cur and j>i:
                self.getsubsets(j, cur + [num], nums, maxlen, record)
        return record
