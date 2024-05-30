class Solution:
    def countOdds(self, low: int, high: int) -> int:
        modifier=1
        if high%2==0 and low%2==0:
            modifier=0
        return (high-low)//2+modifier