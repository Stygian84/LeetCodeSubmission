class Solution:
    def numSplits(self, s: str) -> int:
        res=0
        dc1={}
        dc2={}
        for letter in s:
            dc2[letter]=dc2.get(letter,0)+1

        for i in range(len(s)):
            letter=s[i]
            
            #update dc2
            if letter in dc2:
                dc2[letter]-=1
            if dc2[letter]==0:
                del dc2[letter]
            
            # update dc1
            dc1[letter]=dc1.get(letter,0)+1
            if len(dc1)==len(dc2):
                res+=1
        return res
        