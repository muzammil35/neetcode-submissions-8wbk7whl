class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            prefix = str(len(word)) + '#'
            encoded += prefix + word
        return encoded
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0
        while l < len(s):
            j = s.find('#', l)
            word_len = int(s[l:j])
            decoded.append(s[j+1 : j+1+word_len])

            l = j + 1 + word_len
        return decoded