class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ls=[]
        for rect in rectangles:
            ls.append(min(rect))
        return ls.count(max(ls))
        