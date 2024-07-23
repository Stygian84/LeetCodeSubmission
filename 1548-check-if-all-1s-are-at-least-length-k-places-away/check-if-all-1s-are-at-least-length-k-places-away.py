class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        dist=None
        for item in nums:
            print(dist)
            if item==1:
                if dist and dist<=k:
                    return False
                dist=0
            if dist !=None:
                dist+=1
        return True