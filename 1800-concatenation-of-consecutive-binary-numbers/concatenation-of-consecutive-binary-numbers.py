class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total = []
        for i in range(1,n+1):
            total.append(bin(i)[2:])
        
        total = "".join(total)
        
        return int(total,2)%(10**9+7)