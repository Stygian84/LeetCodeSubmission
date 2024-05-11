class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t)==1:
            return t
            '''
        sorted_s=''.join(sorted(s))
        sorted_t=''.join(sorted(t))
        for idx in range(len(sorted_s)):
            if sorted_s[idx]!=sorted_t[idx]:
                return sorted_t[idx]
        return sorted_t[-1]
        '''
        for letter in t:
            if s.count(letter)!=t.count(letter):
                return letter