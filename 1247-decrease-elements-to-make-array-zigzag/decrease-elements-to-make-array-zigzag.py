class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        even_count=0
        arr=nums[:]
        for i in range(len(nums)):
            if i==0:
                while nums[i]>=nums[i+1]:
                    nums[i]-=1
                    even_count+=1
                continue

            if i%2==0:
                
                if i==len(nums)-1:
                    while nums[i]>=nums[i-1]:
                        nums[i]-=1
                        even_count+=1
                    continue
                while nums[i]>=nums[i-1] or nums[i]>=nums[i+1]:
                    nums[i]-=1
                    even_count+=1
                    
        odd_count=0
        for i in range(len(arr)):
            if i%2==1:
                if i==len(arr)-1:
                    while arr[i]>=arr[i-1]:
                        arr[i]-=1
                        odd_count+=1
                    continue
                while arr[i]>=arr[i-1] or arr[i]>=arr[i+1]:
                    arr[i]-=1
                    odd_count+=1
                    
        if odd_count<even_count:
            return odd_count
        return even_count