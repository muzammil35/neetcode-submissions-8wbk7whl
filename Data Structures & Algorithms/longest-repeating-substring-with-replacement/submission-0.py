class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_map = {}
        l = 0
        r = 0
        max_window = 0

        while r < len(s):

            
            count_map[s[r]] = count_map.get(s[r], 0) + 1

            max_el = max(count_map, key=count_map.get)
            max_el_freq = count_map[max_el]

            if len(s[l:r+1]) - max_el_freq <= k:
                max_window = max(max_window, len(s[l:r+1]))
            else:
                count_map[s[l]] -= 1
                l += 1
                
            r += 1
            

        return max_window
        

