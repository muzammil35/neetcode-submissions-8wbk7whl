class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict={}
        for el in nums:
            if el in nums_dict:
                nums_dict[el] += 1
            else:
                nums_dict[el] = 1
        ret_list = []
        keys_list = list(nums_dict.keys())
        max_copy = list(nums_dict.values())
        for i in range(k):
            ith_max = max(max_copy)
            ret_list.append(keys_list[max_copy.index(ith_max)])
            keys_list.pop(max_copy.index(ith_max))
            max_copy.pop(max_copy.index(ith_max))
        return ret_list

        
        