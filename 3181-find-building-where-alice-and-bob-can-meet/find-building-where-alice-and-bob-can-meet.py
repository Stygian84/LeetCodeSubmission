class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # for each query find the first next greater or equal element than both a,b
        # after index of max(a,b)


        store = []
        for i in range(len(heights)):
            store.append((heights[i],i))
        
        store.sort(key = lambda x:(-x[0],x[1]))

        res = []
        n = len(heights)
        for a,b in queries:
            temp = -1
            if a>b: # make b always the greater one
                a,b=b,a
            if a==b: #if same location, no need to move
                res.append(a)
                continue
            if heights[a]<heights[b]: #if b greater than a, meet at b
                res.append(b)
                continue

            #else find next smallest greater height than both a and b
            smallest_dist = math.inf
            for h,idx in store:
                if h<=heights[b] or h<=heights[a]:
                    break
                if idx<=b:
                    continue
                distance = idx-b
                if distance<smallest_dist:
                    temp = idx
                    smallest_dist = distance

            res.append(temp)
        
        return res