class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        '''result = 0
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                result ^= num
            else:
                nums[num - 1] = -nums[num - 1]
        return result'''
        dc={}
        for num in nums:
            dc[num]=dc.get(num,0)+1
        res=0

        for key,values in dc.items():
            if values==2:
                res^=key

        return res

