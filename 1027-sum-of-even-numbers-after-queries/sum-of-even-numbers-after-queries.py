class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        total=0
        for item in nums:
            if item%2==0:
                total+=item

        for item in queries:

            if nums[item[1]]%2==0:
                total-=nums[item[1]]

            nums[item[1]]+=item[0]
            
            if nums[item[1]]%2==0:
                total+=nums[item[1]]

            res.append(total)
        return res