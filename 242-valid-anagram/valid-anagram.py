class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dc={}
        if len(s)!=len(t):
            return False
        for letter in s:
                dc[letter]=dc.get(letter,0)+1
        for letter in t:
            if letter in dc:
                dc[letter]-=1
        for keys,values in dc.items():
            if values>0:
                return False
        return True
        