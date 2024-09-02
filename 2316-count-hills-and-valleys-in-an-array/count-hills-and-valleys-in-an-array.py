class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        i = 1
        while i < n - 1:
            if nums[i] == nums[i - 1]:
                i += 1
                continue
            
            j = i - 1
            k = i + 1
            while j >= 0 and nums[j] == nums[i]:
                j -= 1
            while k < n and nums[k] == nums[i]:
                k += 1
            
            if j >= 0 and k < n:
                if (nums[i] > nums[j] and nums[i] > nums[k]) or (nums[i] < nums[j] and nums[i] < nums[k]):
                    count += 1
            
            i = k 
        
        return count

