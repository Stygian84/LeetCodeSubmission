class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        i=0

        while i < n-indexDifference:
            item = nums[i]
            j=i+indexDifference
            while j<n:
                if abs(item-nums[j])>=valueDifference:
                    return [i,j]
                j+=1
                
                
            i+=1
        
        return [-1,-1]