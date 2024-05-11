class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for letter in s:
            dic[letter]=dic.get(letter,0)+1
        for key,values in dic.items():
            if values==1:
                return s.index(key)
        return -1