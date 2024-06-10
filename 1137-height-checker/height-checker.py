class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        sorted_heights=sorted(heights)
        for h1,h2 in zip(heights,sorted_heights):
            if h1!=h2:
                count+=1
        return count