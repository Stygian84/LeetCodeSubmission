class Solution:
    def minSwaps(self, s: str) -> int:
        if s=="":
            return 0
        i,j = 0,len(s)-1

        s = list(s)
        op = 0
        cl = 0
        count = 0

        while i<len(s):
            item = s[i]
            if item == "[":
                op+=1
            elif item == "]":
                cl+=1
            if cl>op:
                op+=1
                cl-=1
                while s[j]!="[":
                    j-=1
                s[j],s[i]=s[i],s[j]
                count+=1
            i+=1
        return count

