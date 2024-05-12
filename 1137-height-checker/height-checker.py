class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        sorted_heights=sorted(heights)
        for idx in range(len(heights)):
            if heights[idx]!=sorted_heights[idx]:
                count+=1
        return count