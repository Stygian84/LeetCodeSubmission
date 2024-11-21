class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        



        def calcTotal(arr):
            freq = Counter(arr)
            res = []
            if x>=len(freq):
                return sum(arr)
            
            for k,v in freq.items():
                res.append((v,k))
            
            res.sort(key = lambda x:(-x[0],-x[1]))

            total = 0
        
            for i in range(x):
                total += res[i][0]*res[i][1]
            
            return total


        res = []
        n = len(nums)
        for i in range(n-k+1):
            res.append(calcTotal(nums[i:i+k]))
        return res