class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count=0
        for item in nums:
            if count <0:
                return False
            elif item>count:
                count=item
            count-=1
        return True