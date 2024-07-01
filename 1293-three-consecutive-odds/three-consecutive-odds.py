class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count=0
        for item in arr:
            if item%2==1:
                count+=1
            else:
                count=0
            if count>=3:
                return True
        return False