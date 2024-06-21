class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        fill=1
        count=0
        i=0
        while fill<=n:
            if i<len(nums):
                if nums[i]<=fill:
                    fill+=nums[i]
                    i+=1
                else:
                    fill+=fill
                    count+=1
            else:
                fill+=fill
                count+=1
        
        return count
        