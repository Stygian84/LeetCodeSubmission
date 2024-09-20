class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        length = len(nums)
    
        prefix = [0]*(length+1)
        suffix = [0]*(length+1)

        # 2-2 2-3 2-5
        # 3-2 3-3 3-5
        # 5-2 5-3 5-5
        for i in range(length):
            prefix[i]=prefix[i-1]+nums[i]

        for i in range(length-1,-1,-1):
            suffix[i]=suffix[i+1]+nums[i]
        
        res = []
        #before = current*n - sum of before nums
        #after = sum of after nums - current*m
        #res = before+after

        for i in range(length):
            current = nums[i]
            n = i
            m = length-i-1
            before = current*n - prefix[i-1]
            after = suffix[i+1] - current*m
            res.append(before+after)
            
        return res