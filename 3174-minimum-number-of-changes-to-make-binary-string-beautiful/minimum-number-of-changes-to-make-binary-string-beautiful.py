class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        # count of 0 , count of 1
        
        length = 0
        res = 0
        zero = 0
        one = 0

        for i in range(n):
            length+=1
            if s[i]=="0":
                zero += 1
            else:
                one += 1

            if length == 2:
                length = 0
                if zero == one:
                    res += 1
                zero = 0
                one = 0
                
        return res