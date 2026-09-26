class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set:
                seq = 1
                start = num
                while start + 1 in num_set:
                    seq += 1
                    start += 1
                longest = max(longest, seq)

        return longest
