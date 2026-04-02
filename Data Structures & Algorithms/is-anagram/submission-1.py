class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        if len(s) != len(t):
            return False
        for ind in range(len(s)):
            s_map[s[ind]] = s_map.get(s[ind], 0) + 1
            t_map[t[ind]] = t_map.get(t[ind], 0) + 1

        for key in s_map:
            if key not in t_map:
                return False
            if s_map[key] != t_map[key]:
                return False
        return True

