class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L=0
        R=1
        max_= 1 if len(s)>0 else 0
        seen = []
        if len(s) >0:
            seen.append(s[L])
        while L<len(s)-1 and R<=len(s)-1:
            if s[R] not in seen:
                max_ = max(max_, (R-L)+1 )
                print(s[L:R+1])
                seen.append(s[R])
            else:
                L +=1
                R = L
                seen.clear()
                seen.append(s[L])
            R+=1
        return max_
            
