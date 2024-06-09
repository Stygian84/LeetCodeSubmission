class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = 0
        prefix_sum = 0
        remainder_count = {0: -1}  
        if len(nums)==1:
            return False
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder < 0:
                remainder += k
            
            if remainder in remainder_count:
                if i - remainder_count[remainder] > 1:  return True
            else:
                remainder_count[remainder] = i  
        return count!=0