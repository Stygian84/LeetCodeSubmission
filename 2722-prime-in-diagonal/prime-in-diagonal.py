class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        def isPrime(x):
            if x<=1:
                return False
            if x>1:
                for i in range(2,x):
                    if x%i==0:
                        return False
            return True
        diagonals = []
        n,m = len(nums),len(nums[0])
        for i in range(n):
            for j in range(m):
                if (i==j) or (i+j)==m-1:
                    diagonals.append(nums[i][j])
        res = 0
        for item in diagonals:
            if item>res and isPrime(item):
                res=item
        
        return res