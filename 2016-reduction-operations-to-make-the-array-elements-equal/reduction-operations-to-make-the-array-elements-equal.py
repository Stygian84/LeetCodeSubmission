class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        total=0
        count=0
        prev_num=nums[0]
        
        minimum=nums[-1]
        for num in nums:
            if num!=prev_num:
                total+=count
                prev_num=num
            count+=1
            if num==minimum:
                break

        return total