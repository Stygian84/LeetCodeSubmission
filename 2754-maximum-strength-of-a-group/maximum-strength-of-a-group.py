class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        total=1
        smallest_neg_num=-10
        neg_num_count=0
        zero_count=0

        for num in nums:
            if num==0:
                zero_count+=1
                continue
            total*=num
            if num<0:
                neg_num_count+=1
                smallest_neg_num=max(smallest_neg_num,num)
                
        if neg_num_count % 2 == 1 and total < 0:
            total//=smallest_neg_num
            
        if zero_count>0 and total<0:
            return 0
        if neg_num_count==1 and zero_count>0 and neg_num_count+zero_count==len(nums):
            return 0
        if zero_count==len(nums):
            return 0
        return total