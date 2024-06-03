class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''count= nums.count(val)
        for _ in range(count):
            nums.remove(val)
        return len(nums)'''
        non_val_idx = 0 
        cnt=0
        for num in nums:
            if num != val:
                nums[non_val_idx] = num
                non_val_idx +=1
            else:
                cnt+=1
        return len(nums)-cnt