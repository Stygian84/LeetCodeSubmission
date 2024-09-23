class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        res = []
        for i in range(1,n):
            if height[i-1]>threshold:
                res.append(i)
        return res