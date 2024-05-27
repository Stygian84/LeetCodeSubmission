class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        res=[]
        for item in nums:
            res.append(item**2)
        res.sort()
        return res
        '''
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        idx = n - 1
        
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq >= right_sq:
                res[idx] = left_sq
                left += 1
            else:
                res[idx] = right_sq
                right -= 1
            idx -= 1
        
        return res