class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for i in range(1,n):
            for j in range(i+1,n):
                total=i**2+j**2
                if (total**0.5).is_integer() and total**0.5<=n:
                    count+=1
        return count*2
        