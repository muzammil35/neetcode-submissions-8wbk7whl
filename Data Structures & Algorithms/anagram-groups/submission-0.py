class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_dict = {}
        for word in strs:
            sorted_word_list = sorted(word)
            if "".join(sorted_word_list) in an_dict:
                an_dict["".join(sorted_word_list)].append(word)
            else:
                an_dict["".join(sorted_word_list)] = [word]
        return list(an_dict.values())
        
        
        
        