class Solution:
    def isThree(self, n: int) -> bool:
        count=0
        if n==1:
            return False
        if int((n)**0.5)<n**0.5:
            return False
        
        for i in range(1, int((n)**0.5)):
            if n%i==0:
                count+=2
                if count>2:
                    return False
        return True