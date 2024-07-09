class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1

        
        total_odd=0
        total_even=0
        
        for i in range(n):
            if i%2==0:
                total_even+=nums[i]
            else:
                total_odd+=nums[i]

        current_odd=0
        current_even=0
        count=0

        for i in range(n):
            if i % 2 == 0:
                total_even -= nums[i]
            else:
                total_odd -= nums[i]
            
            if current_even + total_odd == current_odd + total_even:
                count += 1
            
            if i % 2 == 0:
                current_even += nums[i]
            else:
                current_odd += nums[i]

        return count
