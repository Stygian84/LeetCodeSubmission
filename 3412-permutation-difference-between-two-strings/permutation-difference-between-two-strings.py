class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dc1={}
        dc2={}
        for i in range(len(s)):
            dc1[s[i]]=i
            dc2[t[i]]=i
        result=0

        for item in s:
            result+=abs(dc1[item]-dc2[item])
        return result
            
        