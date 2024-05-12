class Solution:
    def maximum69Number (self, num: int) -> int:
        nums=str(num)
        for idx in range(len(nums)):
            if nums[idx]=="6":
                result=nums[:idx]+"9"+nums[idx+1:]
                return int(result)
        return num
        