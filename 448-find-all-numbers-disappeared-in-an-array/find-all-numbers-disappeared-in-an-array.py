class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ls=[]
        for i in range(1,len(nums)+1):
            ls.append(i)
        result=set(ls)-set(nums)
        return list(result)