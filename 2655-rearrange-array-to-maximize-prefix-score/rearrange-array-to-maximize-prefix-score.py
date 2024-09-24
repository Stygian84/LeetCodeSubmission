class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res = [0]*len(nums)


        count=0
        for i in range(len(res)):
            res[i] = res[i-1]+nums[i]
            if res[i]>0:
                count+=1
            else:
                break
        return count