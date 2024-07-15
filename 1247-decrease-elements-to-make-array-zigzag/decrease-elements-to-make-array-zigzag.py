class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        even_count=0
        arr=nums[:]
        for i in range(0,len(nums),2):
            if i==0:
                if nums[i]>=nums[i+1]:
                    diff=nums[i]-nums[i+1]+1
                    nums[i]-=diff
                    even_count+=diff
                continue
            if i==len(nums)-1:
                if nums[i]>=nums[i-1]:
                    diff=nums[i]-nums[i-1]+1
                    nums[i]-=diff
                    even_count+=diff
                continue
            while nums[i]>=nums[i-1] or nums[i]>=nums[i+1]:
                nums[i]-=1
                even_count+=1
                    
        odd_count=0
        for i in range(1,len(arr),2):
            if i==len(arr)-1:
                if arr[i]>=arr[i-1]:
                    diff = arr[i]-arr[i-1]+1
                    arr[i]-=diff
                    odd_count+=diff
                continue
            while arr[i]>=arr[i-1] or arr[i]>=arr[i+1]:
                arr[i]-=1
                odd_count+=1
                    
        if odd_count<even_count:
            return odd_count
        return even_count