class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_ls=[]
        even_ls=[]
        result=[]
        for item in nums:
            if item%2==0:
                even_ls.append(item)
            else:
                odd_ls.append(item)
        for idx in range(len(nums)//2):
            result.append(even_ls[idx])
            result.append(odd_ls[idx])
        return result
