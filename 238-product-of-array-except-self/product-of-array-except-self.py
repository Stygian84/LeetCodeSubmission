class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix_product=[1]*n
        prefix_product2=[1]*n
        '''24 12 8 6
        234 134 124 123
        x 1 12 123
        234 34 4 x'''
        #left to right
        for i in range(len(nums)-1):
            prefix_product[i+1]=prefix_product[i]*nums[i]
        #right to left
        for i in range(len(nums)-1):
            prefix_product2[i+1]=prefix_product2[i]*nums[-i-1]
        prefix_product2.reverse()
        result=[1]*n
        for i in range(n):
            result[i]=prefix_product[i]*prefix_product2[i]
        
        return result
