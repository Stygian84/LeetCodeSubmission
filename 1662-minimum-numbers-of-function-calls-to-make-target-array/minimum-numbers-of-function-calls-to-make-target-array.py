class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #+1 at any index
        # or everyone times 2

        count = 0

        n = len(nums)
        while nums!=[0]*n:
            for i in range(n):
                if nums[i]%2==1:
                    nums[i]-=1
                    count+=1
                nums[i]//=2

            if nums==[0]*n: #if decreasing by 1 result in all zero, return
                return count
            
            count+=1 #for operation 2

        return count