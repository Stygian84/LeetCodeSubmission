class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        dc = defaultdict(int)

        n = len(rectangles)
        count = 0
        for i in range(n):
            w,h = rectangles[i]
            ratio = w/h

            if ratio in dc:
                count+=dc[ratio]
            dc[ratio]+=1
        
        return count