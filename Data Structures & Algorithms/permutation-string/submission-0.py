class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        window = len(s1)
        l = 0
        r = window - 1
        search_map = {}
        string_map = {}
        for char in s1:
            string_map[char] = string_map.get(char,0) + 1
        for char in s2[:window-1]:
            search_map[char] = search_map.get(char, 0) + 1 
        while r < len(s2):

            search_map[s2[r]] = search_map.get(s2[r], 0) + 1

            print(search_map)

            if search_map == string_map:
                return True
            
            else:
                search_map[s2[l]] -= 1
                if search_map[s2[l]] == 0:
                    del search_map[s2[l]]
                l += 1
                r += 1
                

        return False

            



