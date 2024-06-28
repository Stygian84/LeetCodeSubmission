class Solution:
    def minOperations(self, s: str) -> int:
        zero_start,one_start=0,0

        for i in range(len(s)):
            if i%2==0 and s[i]!="0":
                zero_start+=1
            elif i%2==1 and s[i]!="1":
                zero_start+=1

        for j in range(len(s)):
            if j%2==0 and s[j]!="1":
                one_start+=1
            elif j%2==1 and s[j]!="0":
                one_start+=1
        
        return min(zero_start,one_start)