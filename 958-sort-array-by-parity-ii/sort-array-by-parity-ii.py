class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i%2==0:
                counter=0
                while nums[i]%2!=0:
                    nums[i],nums[i+counter]=nums[i+counter],nums[i]
                    counter+=1
            else:
                counter=0
                while nums[i]%2!=1:
                    nums[i],nums[i+counter]=nums[i+counter],nums[i]
                    counter+=1
        return nums
