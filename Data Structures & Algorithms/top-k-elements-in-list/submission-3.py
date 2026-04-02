class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}
        for el in nums:
            if el in nums_dict:
                nums_dict[el] += 1
            else:
                nums_dict[el] = 1
        ret_list = [k_ for k_,v in sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)][:k]
        return ret_list

        
        