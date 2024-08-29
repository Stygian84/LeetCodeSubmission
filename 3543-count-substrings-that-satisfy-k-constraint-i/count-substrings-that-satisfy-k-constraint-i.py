class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        
        i = 0
        one = 0
        zero = 0 
        count = 0

        n = len(s)
        for j in range(n):
            if s[j]=="0":
                zero+=1
            else:
                one+=1
            while zero>k and one>k:
                if s[i]=="1":
                    one-=1
                else:
                    zero-=1
                i+=1
            count+=(j-i+1)
            
        return count