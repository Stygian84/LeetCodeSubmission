class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dc={}
        for letter in s:
            dc[letter]=dc.get(letter,0)+1
        count=0
        for letter in t:
            if dc.get(letter,0)<=0:
                count+=1
            else:
                dc[letter]-=1
        return count