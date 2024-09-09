class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []

        def backtrack(start,path):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        
        backtrack(0,[])
        
        result = 0
        for item in res:
            total = 0
            for num in item:
                total^=num
            result+=total
        return result