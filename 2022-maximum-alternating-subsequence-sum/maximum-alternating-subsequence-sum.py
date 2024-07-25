class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # check increasing -> decreasing -> increasing
        # at increasing find max, at decreasing find min
        total = 0

        increasing = True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if increasing:
                    total+=nums[i-1]
                    increasing = False
            else:
                if not increasing:
                    increasing = True
                    total-=nums[i-1]
        
        if increasing:
            total+=nums[-1]


        return total
        '''odd_sum=[nums[1]]
        even_sum=[nums[0]]
        
        n = len(nums)
        res = 0
        for i in range(2,n):
            if i%2==0:
                even_sum.append(even_sum[-1]+nums[i])
            else:
                odd_sum.append(odd_sum[-1]+nums[i])
            res = max(res,nums[i],even_sum[-1]-odd_sum[-1])
        print(even_sum,odd_sum)

        return res'''