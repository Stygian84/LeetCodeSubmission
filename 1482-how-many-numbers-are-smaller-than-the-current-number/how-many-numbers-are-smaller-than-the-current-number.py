class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        result=[]
        for idx in range(len(nums)):
            count=0
            for item in nums:
                if nums[idx]>item:
                    count+=1
            result.append(count)
        return result
        '''
        dict1={}
        result=[]
        sorted_nums=sorted(nums,reverse=True)
        print(sorted_nums)
        for idx in range(len(sorted_nums)):
            dict1[sorted_nums[idx]]=len(sorted_nums[idx:])-1
        print(dict1)
        for item in nums:
            result.append(dict1[item])
        return result
        