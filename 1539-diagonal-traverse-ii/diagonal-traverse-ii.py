class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ls=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                ls.append((i+j,j,nums[i][j]))
        ls.sort()
        
        res=[]
        for item in ls:
            res.append(item[-1])
        return res