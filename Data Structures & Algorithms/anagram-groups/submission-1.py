class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        anagram_list = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_list:
                ind = anagram_list.index(sorted_word)
            else:
                anagram_list.append(sorted_word)
                ind = len(anagram_list) - 1
            anagrams.setdefault(ind, []).append(word)

        print(anagrams)

        return [k for k in anagrams.values()]