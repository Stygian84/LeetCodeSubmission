class Solution:
    def makeGood(self, s: str) -> str:
        n=len(s)
        for i in range(n//2):
            temp=""
            count=0
            for i in range(len(s)):
                if count>0:
                    count-=1
                    continue
                if i!=len(s)-1 :
                    if (abs(ord(s[i])-ord(s[i+1]))==abs(ord("A")-ord("a"))):
                        count+=1
                        continue
                temp+=s[i]
            s=temp
        return s
        