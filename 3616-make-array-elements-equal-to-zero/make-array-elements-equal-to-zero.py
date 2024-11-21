class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def process(arr,index,direction):
            n = len(arr)
            right = direction
            
            while index<n and index>=0:
                if arr[index]>0:
                    arr[index]-=1        
                    right = not right        
                if right:
                    index+=1
                else:
                    index-=1
            
            return [0]*n==arr
        count = 0

        for i in range(len(nums)):
            if nums[i]==0:
                arr = nums[:]
                count += process(arr,i,True)
            
                arr = nums[:]
                count += process(arr,i,False)
        
        return count