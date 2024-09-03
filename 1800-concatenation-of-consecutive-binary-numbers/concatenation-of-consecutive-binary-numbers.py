class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total = ""
        for i in range(1,n+1):
            total+=bin(i)[2:]
        
        return int(total,2)%(10**9+7)