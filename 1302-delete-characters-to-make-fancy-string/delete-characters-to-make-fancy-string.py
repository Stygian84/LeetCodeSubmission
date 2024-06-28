class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_letter=s[0]
        res=s[0]

        count=0
        for i in range(1,len(s)):
            if s[i]==prev_letter:
                count+=1
            else:
                prev_letter=s[i]
                count=0
            if count<2:
                res+=s[i]
        return res