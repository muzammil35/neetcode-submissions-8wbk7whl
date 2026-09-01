class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        l = 0
        r = 0
        longest = 0
        while l<=r and r<len(s):
            letters[s[r]] = letters.get(s[r],0) + 1
            while letters[s[r]] > 1:
                letters[s[l]] -= 1
                l +=1
            else:
                longest = max(longest, r-l + 1)
                r += 1
        return longest


        